#!/usr/local/bin/python

import sys

def pad_PKCS7(str, leng):
    for i in range(leng-len(str)):
        str += '\x04'
    return str

def main():
    file = open(sys.argv[1], 'r').read().split("\n")
    text = ""
    for line in file:
        text += line

main()
