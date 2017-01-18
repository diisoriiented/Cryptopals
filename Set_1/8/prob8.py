#! /usr/local/bin/python

from base64 import *
from binascii import *
from Crypto.Cipher import AES
from sys import *

def Decrypt_AES_128(input, key):
    ECB = AES.new(key, AES.MODE_ECB)
    return ECB.decrypt(input)

def is_ECB(input):
    blocks = [input[16*i:16*(i+1) ]for i in range(len(input)/16)]
    for block in blocks:
        blocks.remove(block)
        if block in blocks: return True
    return False

def main():
    file = open(argv[1], 'r').read().split("\n")
    for line in file:
        if(is_ECB(line)):
            print(line)

main()
