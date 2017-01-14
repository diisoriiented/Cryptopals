#!/usr/local/bin/python

from binascii import *
from sys import *
from math import *

def h2b(hex):
    return unhexlify(hex)

def b2h(bin):
    return hexlify(bin)

def xor(input, key):
    result = ""
    for ch in input:
        result += chr(ord(ch) ^ key)
    return result

def str_score(str):
    score  = ch_freq("etao", str)
    score = fabs(37.4- score)
    return score

def ch_freq(ch_str, str):
    score = 0
    count = 0
    leng = len(str)
    for char in ch_str:
        count = 0
        for ch in str:
            if ch not in "abcdefghijklmnopqrstuvwxyz' ": return 0
            if char in str:
                count += 1
        score += count/leng
    return score

def crack(input):
    best = 1000
    msg = ""
    for i in range(256):
        result = xor(input, i)
        score = str_score(result.lower())
        if score < best:
            best = score
            msg = result
    return msg


def main():
    hex = h2b(argv[1])
    result = crack(hex)
    print (result)


main()
