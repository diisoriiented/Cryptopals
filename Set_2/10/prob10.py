#!/usr/local/bin/python

import sys
import math
import base64
from Crypto.Cipher import AES

def xor(input, key):
    result = ""
    for ch1, ch2 in zip(input, key):
        result += chr(ord(ch1) ^ ord(ch2))
    return result


#   Changed to encrypto
def EBC_encrypt(input, key):
    ECB = AES.new(key, AES.MODE_ECB)
    return ECB.encrypt(input)

def EBC_decrypt(input, key):
    ECB = AES.new(key, AES.MODE_ECB)
    return ECB.decrypt(input)

def CBC_encrypt(text, key, IV):
    result = ""
    prev = IV
    for i in range(int(math.ceil(len(text)/16.0))):
        block = text[i*16:16*(i+1)]
        ct = EBC_encrypt(xor(block, prev), key)
        result += ct
        prev = ct
    return result

def CBC_decrypt(text, key, IV):
    result = ""
    prev = IV
    for i in range(int(math.ceil(len(text)/16.0))):
        block = text[i*16:16*(i+1)]
        ct = EBC_decrypt(block, key)
        result += xor(ct, prev)
        prev = block
    return result

def pad_PKCS7(str, leng):
    for i in range(leng-len(str)):
        str += '\x00'
    return str

def main():
    file = open(sys.argv[1], 'r').read()
    text = base64.b64decode(file)
    key = "YELLOW SUBMARINE"
    IV = '\x00' * 16
    print(CBC_decrypt(text, key, IV))


main()
