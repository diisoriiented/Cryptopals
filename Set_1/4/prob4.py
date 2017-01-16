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
    score = fabs(37.4-score) #    The closer to 0, the better
    return score

def ch_freq(ch_str, str):
    score = 0.0
    count = 0.0
    str = str.split(' ')
    res_str = ""

    #    ignores spaces in length calculation
    for string in str:
        res_str += string
    leng = len(res_str)
    for char in ch_str:
        count = 0.0 #   Var to calculate frequency
        for ch in res_str:
            if ord(ch) > 127 : return 0 #skips characters that aren't readable ascii
            # print(ch)
            if char == ch:
                count += 1
        score += (count/leng) * 100 #    Frequency calculation
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
    return msg, best


def main():
    global_score = 1000
    msg  = ""
    hex_file = open(argv[1], 'r').read().split('\n')
    for line in hex_file:
        original_hex = line #   Saves original line a.k.a. the answer
        line = h2b(line) #    Converts to binary
        (result,score) = crack(line) #    Should return highest scoring binary string as well as its score
        if score < global_score:
            msg = result
            global_score = score

    print(msg, global_score)
    print(original_hex)
main()
