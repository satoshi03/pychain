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

## Do process for blocks or peers via curl commands

#### Get blocks

```
curl  http://localhost:8080/blocks
```

##### Add block

```
curl --data '{"data" : "Some data to the first block"}' http://localhost:8080/mineBlock
```

##### Get blocks

```
curl http://localhost:8080/blocks
```

##### Add peer

```
curl --data '{"peer" : "ws://localhost:6001"}' http://localhost:8080/mineBlock
```

#### Get peers

```
curl http://localhost:8080/peers
```

# Test

Test pychain code on your environment.

```
pytest -v --flake8 --pep8
```

# License

MIT License
