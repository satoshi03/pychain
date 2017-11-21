import datetime
import hashlib


class Blockchain():

    def __init__(self):
        self.blocks = []
        self.latest_index = -1
        # ジェネシスブロックを追加
        self.add(self.get_genesis_block())

    def __len__(self):
        return len(self.blocks)

    def __repr__(self):
        return str(self.blocks)

    def add(self, block=None, data=None):
        # blockとdataの両方がNoneならば何もしない
        if not (block or data):
            print("error: add with no args")
            return

        # blockが指定されていない場合
        if not block:
            index = self.latest_index + 1
            previous_hash = self.blocks[-1].hash  # 最後尾のブロックのhashを取得
            timestamp = datetime.datetime.now()
            hash = Block.calc_hash_from_args(index, previous_hash, timestamp, data)
            block = Block(index, previous_hash, timestamp, data, hash)

        # blockが有効ならばblocksに追加
        if len(self.blocks) == 0 or block.is_valid(self.blocks[-1]):
            self.blocks.append(block)
            self.latest_index += 1
        return

    def replace(self, blockchain):
        if blockchain.is_valid() and len(blockchain) > len(self):
            self.blocks = blockchain.blocks
            self.latest_index = blockchain.blocks[-1].index

    def is_valid(self):
        if str(self.blocks[0]) != str(self.get_genesis_block()):
            print("invalid genesis block")
            return False

        for bl in self.blocks:
            if bl.index != 0 and not bl.is_valid(self.blocks[bl.index-1]):
                print("block invalid")
                return False

        return True

    def get_genesis_block(self):
        return Block(
            0,
            "0",
            1465154705,
            "my genesis block!!",
            "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7"
        )


class Block():

    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return str(self.index)+self.previous_hash+str(self.timestamp)+self.data+self.hash

    def is_valid(self, pre_block):
        if pre_block.index + 1 != self.index:
            print("error: invalid index")
            return False
        if pre_block.hash != self.previous_hash:
            print("error: invalid previous_hash")
            return False
        if self.calc_hash() != self.hash:
            print("error: invalid hash")
            return False
        return True

    def calc_hash(self):
        return Block.calc_hash_from_args(self.index, self.previous_hash, self.timestamp, self.data)

    @staticmethod
    def calc_hash_from_args(index, previous_hash, timestamp, data):
        return hashlib.sha256(
            (str(index)+previous_hash+str(timestamp)+str(data)).encode('utf-8')
        ).hexdigest()
