# -*- coding:utf-8 -*- 
__author__ = 'wangxuan'

# https://learnblockchain.cn/2017/10/27/build_blockchain_by_python/#more

# Blockchain 用来管理链条，它能存储交易，加入新块等
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass
