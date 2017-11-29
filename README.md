# pychain

Pychain is an implementation of Naivechain in Python3 

# Getting Started

Download pytest on your local directory.

```
git clone https://github.com/satoshi03/pychain.git
```

Install dependencies.

```
cd <project dir>
pip install -r requirements.txt
```

# How to run pychain server in development environment

Run server on 8080 port as default

```
python main.py
```

Get blocks via curl command

```
curl  http://localhost:8080/blocks
```

Add block via curl command

```
curl --data '{"data" : "Some data to the first block"}' http://localhost:8080/mineBlock
```

# Test

Test pychain code on your environment.

```
pytest -v --flake8 --pep8
```

# License

MIT License
