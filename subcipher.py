# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 11:07:37 2014

Usage:
  subcipher.py -g outfile
  subcipher.py -e infile outfile keyfile
  subcipher.py -d infile outfile keyfile

@author: bmkessle
"""

from math import factorial
from random import randrange
import argparse

DEFAULTCHARSET = [chr(i) for i in range(32,127)]+['\t','\n']

def kth_permutation(items, k):
    _items = list(items)
    if(k=>factorial(len(_items))):
        raise ValueError('k must be less than factorial(len(items)))')
    result = []
    for n in reversed(range(len(_items))):
        base =  factorial(n)
        digit  = k / base
        result.append(_items.pop(digit))
        k %= base
    return result
    
def encode_string(instring,code_dict):
    return ''.join(map(lambda x: code_dict.get(x,x),instring))

def encode_file(infile,outfile,code_dict):
    with open(infile,'r') as f:
        instring = f.read()
    outstring = encode_string(instring,code_dict)
    with open(outfile,'w') as f:
        f.write(outstring)

def generate_keyfile(keyfile,codesymbols):
    key = randrange(factorial(len(codesymbols)))
    with open(keyfile,'w') as f:
        f.write(str(key))
    return key
    
def read_keyfile(keyfile):
    with open(keyfile,'r') as f:
        key = f.read()
    return int(key)
    
def generate_encoding_dict(key,codesymbols):
    code_dict = dict((a,b) for a,b in zip(codesymbols,kth_permutation(codesymbols, key)))
    return code_dict

def generate_decoding_dict(key,codesymbols):
    code_dict = dict((b,a) for a,b in zip(codesymbols,kth_permutation(codesymbols, key)))
    return code_dict
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program for encoding/decoding text files (ascii) using a simple substitution cipher with the substitution indexed by an integer key')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g', action='store', dest='keyfile',help='Generate a key and save it to keyfile')
    group.add_argument('-e', action='store', nargs=3, metavar=('INFILE','OUTFILE','KEYFILE'),help='Encode the text in infile and save to outfile using the key in keyfile')
    group.add_argument('-d', action='store', nargs=3, metavar=('INFILE','OUTFILE','KEYFILE'),help='Decode the text in infile and save to outfile using the key in keyfile')
    args = parser.parse_args()
    codesymbols = DEFAULTCHARSET
    if args.keyfile:
        print 'Generating key...'
        key = generate_keyfile(args.keyfile,codesymbols)
        print 'Key:',key
        print 'Saved to file:',args.keyfile
    elif args.e:
        infile,outfile,keyfile = args.e
        print 'Encoding file',infile,'using keyfile',keyfile
        key = read_keyfile(keyfile)
        code_dict = generate_encoding_dict(key,codesymbols)
        encode_file(infile,outfile,code_dict)
        print 'Encoded file saved to:',outfile
    elif args.d:
        infile,outfile,keyfile = args.d
        print 'Decoding file',infile,'using keyfile',keyfile
        key = read_keyfile(keyfile)
        code_dict = generate_decoding_dict(key,codesymbols)
        encode_file(infile,outfile,code_dict)
        print 'Decoded file saved to:',outfile
    else:
        parser.print_help()