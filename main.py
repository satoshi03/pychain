import json
import socket
from urllib.parse import urlparse
from multiprocessing import Process

from bottle import post, get, run, request

from blockchain import Blockchain
from server import Peer
from const import QUERY_LATEST

blockchain = Blockchain()

peers = []


@post('/mineBlock')
def mine_block():
    dic = json.load(request.body)
    blockchain.add(data=dic["data"])
    msg = {
        "type": QUERY_LATEST,
        "data": blockchain.blocks[-1].to_dict()
    }
    broadcast(json.dumps(msg))
    return


@get('/blocks')
def get_blocks():
    json_blockchain = blockchain.to_json()
    return json_blockchain


@post('/addPeer')
def add_peer():
    dic = json.load(request.body)
    url = urlparse(dic["peer"])
    s = socket.socket()
    try:
        s.connect((url.hostname, url.port))
        peers.append(Peer(url.hostname, url.port, s))
    except ConnectionRefusedError:
        print("socoket connection error")
        s.close()


@get('/peers')
def get_peers():
    json_peers = json.dumps([str(p) for p in peers])
    return json_peers


def broadcast(data):
    for peer in peers:
        peer.send(data)


def start_httpserver():
    run(host='localhost', port=8080)


p = Process(target=start_httpserver)
p.start()

s = socket.socket()

port = 5000
s.bind(('', port))

while True:
    print("listening")
    s.listen(5)
    c, addr = s.accept()
    print('receiving')
    print(c.recv(4096))
    c.close()
s.close()
p.join()
