from django.db import models

# Entities

class Cafe(models.Model):
    # You don't need to add custom primary key. Database will use surrogate key.
    # business_id = models.AutoField(verbose_name="업장번호", primary_key=True)
    brand_name = models.CharField(verbose_name="상호명", max_length=50)
    membership = models.ManyToManyField(verbose_name="멤버십", to="cafe.Customer",
                                        through="cafe.Membership", related_name="membership_place")

class Employee(models.Model):
    # employee_id = models.AutoField(verbose_name="직원번호", primary_key=True)
    name = models.CharField(verbose_name="이름", max_length=50)
    job = models.CharField(verbose_name="직급", max_length=100)

class Menu(models.Model):
    # menu_id = models.AutoField(verbose_name="메뉴번호", primary_key=True)
    name = models.CharField(verbose_name="이름", max_length=100)
    price = models.IntegerField(verbose_name="가격")

class Customer(models.Model):
    # customer_id = models.AutoField(verbose_name="고객번호", primary_key=True)
    name = models.CharField(verbose_name="이름", max_length=50)

# Relationships

class Employ(models.Model):
    # register_id = models.AutoField(verbose_name="등록번호", primary_key=True)
    place = models.ForeignKey(verbose_name="고용사업장", to='cafe.Cafe',
                              on_delete=models.CASCADE, related_name='employ')
    employee = models.OneToOneField(verbose_name="피고용인", to='cafe.Employee',
                                    on_delete=models.CASCADE, related_name='employ')
    employ_date = models.DateField(verbose_name="고용일자") # Employee table exists for this attribute.


class Order(models.Model):
    # order_id = models.AutoField(verbose_name="주문번호", primary_key=True)
    place = models.ForeignKey(verbose_name="업장", to="cafe.Cafe",
                              on_delete=models.CASCADE, related_name="order")
    customer = models.ForeignKey(verbose_name="고객", to="cafe.Customer", null=True,
                                 on_delete=models.SET_NULL, related_name="order")
    menu = models.ManyToManyField(verbose_name="주문 메뉴", to="cafe.Menu",
                                  through="cafe.Sell", related_name="order")
    total_price = models.IntegerField(verbose_name="총 금액")


class Sell(models.Model):
    # sell_id = models.AutoField(verbose_name="판매번호", primary_key=True)
    product = models.OneToOneField(verbose_name="제품", to="cafe.Menu", null=True,
                                   on_delete=models.SET_NULL, related_name="sell_history")
    order = models.ForeignKey(verbose_name="주문", to="cafe.Order",
                              on_delete=models.CASCADE, related_name="sell_history")
    sell_at = models.DateTimeField(verbose_name="판매일시", auto_now_add=True)


class Membership(models.Model):
    # membership_id = models.AutoField(verbose_name="멤버십번호", primary_key=True)
    place = models.ForeignKey(verbose_name="업장", to="cafe.Cafe",
                              on_delete=models.CASCADE, related_name="member")
    customer = models.ForeignKey(verbose_name="멤버십 고객", to="cafe.Customer",
                                 on_delete=models.CASCADE, related_name="membership")
