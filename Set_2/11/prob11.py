#!/usr/local/bin/python

import sys
import math
import base64
from Crypto.Cipher import AES
from Crypto.Random import random

def xor(input, key):
    result = ""
    pad_PKCS7(input, AES.block_size)
    pad_PKCS7(key, AES.block_size)
    for ch1, ch2 in zip(input, key):
        result += chr(ord(ch1) ^ ord(ch2))
    return result


def EBC_encrypt(input, key):
    ECB = AES.new(key, AES.MODE_ECB)
    if len(input) % AES.block_size != 0:
        input += '\x00' * (16 - (len(input) % AES.block_size))
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

def rand_key(block_size):
    key = ""
    for i in range(block_size):
        key += str(random.randint(0,1))
    return key

def is_ECB(input):
    blocks = [input[16*i:16*(i+1) ]for i in range(len(input)/16)]
    for block in blocks:
        blocks.remove(block)
        if block in blocks: return True
    return False

def encryption_oracle(input):
    key = rand_key(AES.block_size)
    EBC_OR_CBC = random.randint(1,2)
    input += chr(random.randint(0,255)) * random.randint(5,10)
    input = chr(random.randint(0,255)) * random.randint(5,10) + input
    actual = "EBC" if EBC_OR_CBC == 1 else "CBC"
    if EBC_OR_CBC == 1:
        data = EBC_encrypt(input, key)
    else:
        IV = rand_key(AES.block_size)
        data = CBC_encrypt(input, key, IV)
    if is_ECB(data):
        print("Guess: ECB - Actual: %s") % (actual)
    else:
        print("Guess: CBC - Actual: %s") % (actual)
    return

def main():
    text = base64.b64decode(open(sys.argv[1], 'r').read())
    encryption_oracle(text)


main()
