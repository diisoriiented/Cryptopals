#!/usr/local/bin/pythonw
from sys import *
from math import *

def hamming_dist (s1, s2):
    count = 0
    for ch1, ch2 in zip(s1, s2):
        b1 = bin(ord(ch1))
        b2 = bin(ord(ch2))
        for bit1, bit2 in zip(b1, b2):
            if bit1 != bit2: count += 1
    count += 4 * (fabs(len(s1)-len(s2)))
    return count

def main():
    #print(hamming_dist("this is a test", "wokka wokka!!!\n")) -- works correctly (answer is 37)

main()
