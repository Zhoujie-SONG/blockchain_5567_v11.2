# coding:utf-8
from blocks.block import Block
from const.const import Const
import time
from transaction import Vout, Transaction
from account import get_account
from database import BlockChainDB, TransactionDB, UnTransactionDB
from lib.common import unlock_sig, lock_sig
from Company import Company
# @Written by LI Zijie 2022/11/23 16:25

# Instantiation
comp1 = Company(0)
history_messages = []
def reward():
    reward = Vout(get_account()['address'], Const.REWARD)
    tx = Transaction([], reward)
    return tx

def coinbase():
    """
    First block generate.
    """
    rw = reward()
    cb = Block(0, int(time.time()), [rw.hash], "")
    # nonce = cb.pow()
    nonce = cb.proof_of_work()
    cb.make(nonce)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    TransactionDB().insert(rw.to_dict())
    return cb

def get_all_untransactions():
    UnTransactionDB().all_hashes()

def mine():
    """
    Main miner method.
    """
    # Found last block and unchecked transactions.
    global history_messages
    last_block = BlockChainDB().last()
    if len(last_block) == 0:
        last_block = coinbase().to_dict()
    untxdb = UnTransactionDB()
    # Miner reward
    rw = reward()
    untxs = untxdb.find_all()
    untxs.append(rw.to_dict())
    # untxs_dict = [untx.to_dict() for untx in untxs]
    untx_hashes = untxdb.all_hashes()
    # Clear the untransaction database.
    untxdb.clear()

    # # 创建新块
    # new_block = Block(last_block['index'] + 1, int(time.time()), untx_hashes, last_block['hash'])
    # # 设定新区块的pre_difficulty和difficulty
    # new_block.set_difficulty()
    # new_block.get_merkleroot()
    # # 通过pow计算出new_block的nonce值存入loop_flag, 如果pow时index重复，则nonce返回-1
    # loop_flag = new_block.proof_of_work()

    # Miner reward is the first transaction.
    untx_hashes.insert(0,rw.hash)


    comp1.PrepareData()
    message= comp1.PrepareData()
    # Num_Upload = {str(comp1.Seq_company):str(comp1.Num_Upload)}
    a = str(comp1.Seq_company)
    b = str(comp1.Num_Upload)

    cb = Block(last_block['index'] + 1, int(time.time()), untx_hashes, last_block['hash'], message, history_messages, a, b)
    history_messages = cb.add_message(message)

    # nonce = cb.pow()
    nonce = cb.proof_of_work()


    cb.make(nonce)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    TransactionDB().insert(untxs)
    # Broadcast to other nodes
    Block.spread(cb.to_dict())
    Transaction.blocked_spread(untxs)
    return cb