#! /usr/local/bin/python

from base64 import *
from binascii import *
from Crypto.Cipher import AES
from sys import *

def Decrypt_AES_128(input, key):
    ECB = AES.new(key, AES.MODE_ECB)
    return ECB.decrypt(input)

def main():
    file = open(argv[1], 'r').read()
    text = b64decode(file)
    key = "YELLOW SUBMARINE"
    result = Decrypt_AES_128(text, key)
    print(result)

main()
