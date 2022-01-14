from django.db import models

# Entities

class Cafe(models.Model):
    # You don't need to add custom primary key. Database will use surrogate key.
    # business_id = models.AutoField(verbose_name="업장번호", primary_key=True)
    brand_name = models.CharField(verbose_name="상호명", max_length=50)

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
