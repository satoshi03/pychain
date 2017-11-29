import json

from bottle import post, get, run, template, request

from blockchain import Blockchain

blockchain = Blockchain()


@post('/mineBlock')
def mine_block():
    dic = json.load(request.body)
    blockchain.add(data=dic["data"])
    return


@get('/blocks')
def get_blocks():
    json_blockchain = blockchain.to_json()
    return template(json_blockchain)


run(host='localhost', port=8080)
