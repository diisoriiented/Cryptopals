#!/usr/local/bin/pythonw

from sys import *
from math import *
from binascii import *
from base64 import *
import itertools

def pad_bin(bin):
    if len(bin) < 8:
        bin = (7-(len(bin)))*"0" + bin
        return bin

def hamming_dist (s1, s2):
    count = 0 
    for ch1, ch2 in zip(s1, s2):
        b1 = pad_bin(bin(ord(ch1))[2:])
        b2 = pad_bin(bin(ord(ch2))[2:])
        for bit1, bit2 in zip(b1, b2):
            if bit1 != bit2: count += 1.0
    return float(count)

def get_keysize(input):
    smallest_ham = 1000 #   Sets an arbitrary value for hamming distance
    keysize = 0         #   Starts keysize at 0... arbitrary
    for size in range(2,min(40,len(input)/4)):
        strs = [input[size*i:size*(i+1)] for i in range(4)]
        pairs = [pair for pair in itertools.combinations(strs, 2)]
        NORM_HAM_DIST = 0
        for pair in pairs:
            NORM_HAM_DIST += float(hamming_dist(pair[0],pair[1])/size)
        NORM_HAM_DIST /= len(pairs)
        if NORM_HAM_DIST < smallest_ham:
            smallest_ham = NORM_HAM_DIST
            keysize = size  #   Sets keysize to be the smallest average hamming distance
    return keysize

def xor(input, key):
    result = ""
    for ch in input:
        result += chr(ord(ch) ^ key)
    return result

def str_score(str):
    score  = ch_freq("abcdefghijklmnopqrstuvwxyz", str)
    score = fabs(100-score)    #   Relative frequency of "etao" in english
    return score

def ch_freq(ch_str, str):
    score = 0.0
    count = 0.0
    str = str.split(' ')
    res_str = ""
    for string in str:
        res_str += string
    leng = len(res_str)
    for char in ch_str:
        count = 0.0
        for ch in res_str:
            if ord(ch) > 127: return 0
            # print(ch)
            if char == ch:
                count += 1
        score += (count/leng) * 100
    return score

#   Altered xor crack function for rep_xor (returning best key)
def crack(input):
    best = 1000
    best_key = None
    msg = ""
    for i in range(256):
        result = xor(input, i)
        score = str_score(result.lower())
        if score < best:
            best = score
            best_key = i
            msg = result
    return best_key

def rep_xor(key, input):
    result = ""
    counter = 0
    leng = len(key)
    numtimes = 0
    for ch in input:
        if counter == leng: counter = 0
        result += chr(ord(ch) ^ ord(key[counter]))
        counter += 1
    return result

def main():
    #print(hamming_dist("this is a test", "wokka wokka!!!")) #-- works correctly (answer is 37)

    #   Opens file, and splits it by '\n' character, then adds it to a single string

    file = open(argv[1], 'r').read()
    text = b64decode(file)  #   Converts from base64 to ascii

    KEYSIZE = get_keysize(text) # Gets keysize using hamming distance

    #   Step 6, adding arrays of blocks of 5
    block_arr = []
    block_text = ""
    counter = 0
    for c in text:
        if counter == KEYSIZE:
            counter = 0
            block_arr.append(block_text)
            block_text = ""
        block_text += c
        counter += 1
    block_arr.append(block_text) # last line in the file


    #   Transposing the blocks
    block_transpose = [""] * KEYSIZE
    counter = 0
    for str in block_arr:
        for c in str:
            block_transpose[counter] += c
            counter += 1
        counter = 0


    counter = 0
    key = ""
    for str in block_transpose:
        key += chr(crack(str))
    print("Key : {%s}") % (key)
    print(rep_xor(key, text))

main()
