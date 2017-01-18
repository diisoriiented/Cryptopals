#!/usr/local/bin/python

import sys

def pad_PKCS7(str, leng):
    for i in range(leng-len(str)):
        str += '\x04'
    return str

def main():
    padded_str = pad_PKCS7("YELLOW SUBMARINE", 20)


main()
