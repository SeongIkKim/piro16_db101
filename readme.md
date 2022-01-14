# Repository Guide

## Requirements

- python(>=3.8)

## Milestones


- [ ] [Optional] Install graphviz. It varies to your os.
  - For Windows : See [this link](https://hengbokhan.tistory.com/153), and [documentation](https://pygraphviz.github.io/documentation/stable/install.html#manual-download).
  - For Mac OS : Use Homebrew.
    ```bash
    $ brew install graphviz 
    ```
- [ ] Install requirements (`pip install -r requirements.txt`)
- [ ] Add model schemas.
- [ ] Make migration files and migrate them.
- [ ] [Optional] Visualize them by `pygraphviz`.
  ```bash
  $ python3 manage.py graph_models cafe -o cafe_er_diagram.png 
  ```
