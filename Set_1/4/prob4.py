#!/usr/local/bin/pythonw

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
            if ch not in "abcdefghijklmnopqrstuvwxyz' ?\".,-;:!": return 0
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
        #print(result)
        if score < best:
            best = score
            msg = result
    return msg, best


def main():
    best = 0
    msg  = ""
    hex_file = open(argv[1], 'r').read().split('\n')
    for line in hex_file:
        line = h2b(line)
        (result,score) = crack(line)
        if score > best:
            msg = result
            best = score
    print(msg)
    print(best)
main()
