#!/usr/local/bin/python

import binascii
import sys

def hex_to_b64(hex):
    binary = binascii.unhexlify(hex)
    b64 = binascii.b2a_base64(binary)
    return b64

def main():
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64 = hex_to_b64(hex)
    print(b64)

main()
