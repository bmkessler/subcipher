# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 07:22:31 2014

Usage:
  ontetimepad.py -e infile outfile
  ontetimepad.py -d infile outfile

@author: bmkessle
"""
    
from os import urandom
import argparse

def encode_text(text,otp):
    return [b1^b2 for b1,b2 in zip(text,otp)]

def read_file(filename):
    with open(filename,'rb') as f:
        b_array = bytearray(f.read())
    return b_array

def write_file(filename,data):
    with open(filename,'wb') as f:
        for b in data:
            f.write(chr(b))

def generate_otp(N):
    return bytearray(urandom(N))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program for encoding/decoding text files (ascii) using a one-time pad')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', action='store', nargs=2, metavar=('INFILE','OUTFILE'),help='Encode the text in infile and save to outfile storing the one-time pad in outfile.otp')
    group.add_argument('-d', action='store', nargs=2, metavar=('INFILE','OUTFILE'),help='Decode the text in infile and save to outfile using the one-time pad in infile.otp')
    args = parser.parse_args()
    if args.e:
        infile,outfile = args.e
        otpfile = outfile+'.otp'
        print 'Encoding file:',infile,'using one-time pad...'
        text = read_file(infile)
        otp = generate_otp(len(text))
        encoded_text = encode_text(text,otp)
        write_file(outfile,encoded_text)
        print 'Encoded file saved to:',outfile
        write_file(otpfile,otp)
        print 'Onetime pad file saved to:',otpfile
    elif args.d:
        infile,outfile = args.d
        otpfile = infile+'.otp'
        print 'Decoding file:',infile,'using one-time pad:',otpfile
        text = read_file(infile)
        otp = read_file(otpfile)
        decoded_text = encode_text(text,otp)
        write_file(outfile,decoded_text)
        print 'Decoded text:\n',''.join(map(chr,decoded_text)),'\n'
        print 'Decoded file saved to:',outfile
    else:
        parser.print_help()