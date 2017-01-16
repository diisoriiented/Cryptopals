#!/usr/local/bin/pythonw
from sys import *
from binascii import *
def rep_xor(key, input):
    result = ""
    counter = 0
    leng = len(key)
    numtimes = 0
    for ch in input:
        if counter == leng: counter = 0
        print("Char: %s -- Key: %s") % (ch, key[counter])
        result += chr(ord(ch) ^ ord(key[counter]))
        counter += 1
    return result

def main():
    file = open(argv[1], 'r')
    out_file = open(argv[2], 'w')
    rep_key = argv[3]
    input = ""
    for line in file:
        input += line
    input = input.rstrip()
    result = rep_xor(rep_key, input)
    result = hexlify(result)
    out_file.write(result)
    out_file.write("\n")
main()
