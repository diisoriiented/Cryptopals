#!/usr/local/bin/python

from binascii import *
import sys

def h2b(hex):
    return unhexlify(hex)

def b2h(bin):
    return hexlify(bin)

def usage():
    print("Strings should be the same length")
    exit()

def xor(bin1, bin2):
    result = ""
    for ch1, ch2 in zip(bin1, bin2):
        result += chr(ord(ch1) ^ ord(ch2))
    return result

def main():
    if len(sys.argv[1]) != len(sys.argv[2]):
        usage()
    b1 = h2b(sys.argv[1])
    b2 = h2b(sys.argv[2])

    res = b2h(xor(b1, b2))

    print("%s xor'ed with %s is: %s") % (sys.argv[1], sys.argv[2], res)

main()
