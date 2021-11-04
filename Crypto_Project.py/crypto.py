import hashlib
from time import time

from Crypto.Signature import *


class Blockchain (object):
    def__init__(self):
        self.chain = []


def getLastBlock(self):
        return self.chain[-1];

    def addBlock(self, block):
        if(len(self.chain) > 0):
            block.prev = self,getLastBlock().hash;
        else:
            block.prev = "none";
        self.chain.append(block)


class Block (object):
    def__init__(self, transactions, time, index):
        self.index = index
    self.transactions = transactions
self.time = time
self.prev = ''
self.hash = self.calculateHash()


def calculateHash(self):
        hashTransactions = "";
        for transactions in self.transactions:
            hashTransactions += transactions.hash

        hashString = str(self,time) + hashTransactions + self.prev + str(self.index)
        hashEncoded = jason.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha3_256(hashEncoded).hexdigest(); # ETH Hash


class Transaction (object):
    def__init__(self, sender, reciever, amt):\
        self.sender = sender;
        self.reciever = reciever;
        self.amt = amt;
        self.time = time();
        self.hash = self.calculateHash();

    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time);