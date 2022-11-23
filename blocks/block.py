import hashlib
import time
from datetime import datetime
# from Database.mongoDB import MongoDB
from utils.crypto import Crypto
from const.const import Const
from model import Model
from rpc import BroadCast

# @Written by LI Zijie 2022/11/23 16:25

class Block(Model):


    def __init__(self, index, timestamp, tx, previous_hash,  message, messages, Seq_Company, Num_Upload):
        self.index = index
        self.timestamp = timestamp
        self.tx = tx
        self.previous_block = previous_hash
        self.curr_message = message
        self.messages = messages
        self.Upload_Record = {Seq_Company: Num_Upload}
        # self.dynamic_difficulty = dynamic_difficulty

    # def

    def add_message(self, message) -> str:
        # if len(self.messages) > 0:
        #     message.link(self.messages[-1])
        # message.seal()
        self.messages.append(message)
        return self.messages
        # j = self.curr_message
        # for i in self.messages:
        #     self.messages = hashlib.sha256(str(i+j).encode('utf-8')).hexdigest()
            # self.messages.append(message)

    def header_hash(self):
        """
        Refer to bitcoin block header hash
        """
        return hashlib.sha256((str(self.index) + str(self.timestamp) + str(self.tx) + str(self.previous_block)).encode(
            'utf-8')).hexdigest()

    def pow(self):
        """
        Proof of work. Add nonce to block.
        """
        nonce = 0
        while self.valid(nonce) is False:
            nonce += 1
        self.nonce = nonce
        return nonce

    def make(self, nonce):
        """
        Block hash generate. Add hash to block.
        """
        self.hash = self.ghash(nonce)

    def ghash(self, nonce):
        """
        Block hash generate.
        """
        header_hash = self.header_hash()
        token = ''.join((header_hash, str(nonce))).encode('utf-8')
        return hashlib.sha256(token).hexdigest()

    def valid(self, nonce):
        """
        Validates the Proof
        """
        return self.ghash(nonce)[:4] == "0000"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, bdict):
        b = cls(bdict['index'], bdict['timestamp'], bdict['tx'], bdict['previous_block'])
        b.hash = bdict['hash']
        b.nonce = bdict['nonce']
        return b

    @staticmethod
    def spread(block):
        BroadCast().new_block(block)

    def pow(self):
        """
        Proof of work. Add nonce to block.
        """
        nonce = 0
        while self.valid(nonce) is False:
            nonce += 1
        self.nonce = nonce
        return nonce

    def valid(self, nonce):
        """
        Validates the Proof
        """
        return self.ghash(nonce)[:4] == "0000"

    # POW, return the final nonce which satisfy the computing task
    def proof_of_work(self):
        # 使用难度difficulty获取难度目标target
        # target = 2 ** (256 - 12)
        difficulty = self.dynamic_difficulty(Const.BASE_DIFFICULTY)
        # test lines
        print("POW gets difficulty: " + str(difficulty))
        target = 2 ** (256 - difficulty)
        # test lines
        print("Calculate target: " + str(target))
        time.sleep(2)

        # target = 2 ** (256 - Const.BASE_DIFFICULTY)
        # 执行迭代，nonce+1 直到找到满足目标的随机数
        for nonce in range(Const.MAX_NONCE):

            header_bin = (str(self.index) + str(self.timestamp) + str(self.tx) + str(self.previous_block)) + str(nonce)
            # header_bin = str(self.index) + str(self.timestamp) + str(self.prevHash) + str(self.difficulty) + str(
            #     nonce) + str(self.data) + str(self.merkleroot)

            # test lines
            print("Header_bin: " + str(header_bin))
            print("Nonce: " + str(nonce))
            time.sleep(2)

            hash_res = Crypto().sha256(Crypto().sha256(header_bin))
            # print('\n' + hash_res)
            # hash_res = hashlib.sha256((str(self.hash_txs()) + str(nonce)).encode('utf-8')).hexdigest()
            # 如果index重复，则不进行后续步骤返回nonce值为-1
            # if (self.index_comparison() == 1):
            #     # test 2: 计算的nonce值
            #     print("Proof of work alogrithm calculates nonce = -1")
            #     return -1

            # test lines
            print("Hash_res: " + str(hash_res))

            if int(hash_res, 16) < target:
                # test 2: 计算的nonce值
                print("Proof of work alogrithm calculates nonce =" + str(nonce))
                self.nonce = nonce
                return nonce
        # 即使遍历所有随机数也无法满足目标
        print(f'failed after {Const.MAX_NONCE} tries')
        return -1

    # change 1: Adds a new initial property

    # change 2: Added the case where the block is a new block

    # set the difficulty of this block
    # def set_difficulty(self):
    #     # get the previous block's difficulty
    #     last_block = {}
    #     for x in MongoDB().getlast('blockchain'):
    #         last_block = x
    #         pre_difficulty = x['difficulty']
    #     # if this block is the first block, set the difficulty with the default value
    #     if len(last_block) == 0:
    #         pre_difficulty = const.BASE_DIFFICULTY
    #         # using func dynamic_difficulty and previous block's difficulty to compute this block's difficulty
    #     self.difficulty = self.dynamic_difficulty(pre_difficulty)
    #     # print("set difficulty")
    #     MongoDB().close_connect()

    # change 3: Added the case where the block is in the range of the first 10 blocks

    # this func is used to change the difficulty dynamically
    def dynamic_difficulty(self, difficulty):
        # the supposed time of mining one block
        expected_time = Const.BASE_MINETIME

        # get present and previous timescamps
        # if index > 10 and index % 10 == 1:
        #     dynamic_difficulty = last_block.dynamic_difficulty * \
        #                          (self.blockchain.blocks[height - 1].timestamp -
        #                           self.blockchain.blocks[height - 10].timestamp) / 5 * 10
        timescamp_t1 = 1
        timescamp_t2 = 10


        timescamp_t1 = self.Block[index - 10].timestamp
        timescamp_t2 = self.Block[index - 1].timestamp


        # get the timestamp of the previous tenth block
        # b = MongoDB().getlastn('blockchain', 10)
        # timelist = []
        # for x in b:
        #     timelist.append(x['timestamp'])
        #     # print(x['timestamp'])
        # MongoDB().close_connect()
        # # set the first 10 blocks' difficulty with the default value
        # if (len(timelist) < 10):
        #     return Const.BASE_DIFFICULTY
        # # print(len(timelist))
        # timescamp_t1 = timelist[-1]
        # # 当前最新挖掘出来的区块的时间戳是timescamp_t2
        # timescamp_t2 = self.timestamp



        # 实际挖掘间隔是actual_time,将其与excepted_time进行比较
        actual_time = (timescamp_t2 - timescamp_t1) / Const.ADJUSTMENT_NUM
        # 这里可以设计一个偏离度deviation，计算基于基准的偏差。在挖掘用户数量变化大的时候可以加速调整difficulty。
        # set deviation
        deviation = 1 + abs(actual_time - expected_time) / expected_time
        # factor为difficulty的调整上下限。
        if (actual_time > expected_time * Const.UPPER_LIMIT):
            difficulty = round(Const.BASE_DIFFICULTY * deviation)
        if (actual_time < expected_time * Const.LOWER_LIMIT):
            difficulty *= round(Const.BASE_DIFFICULTY * deviation)
        if difficulty < 0:
            difficulty = 0
        # 返回经过调整的动态difficulty值

        # test 1: 计算的difficulty值
        print("Dynamic difficulty algorithm returns =" + str(difficulty))

        return difficulty

