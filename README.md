subcipher
=========

A project for playing around with substitution ciphers and one-time pads.  Note, this project is not intended for actually cryptography applications, but just for fun and education.

subcipher.py is a simple script for encoding and decoding simple substitution ciphers.  It relies on a numeric "key" identifying the permutation of the character set.

onetimepad.py generates a one-time pad the same length as the file and encodes the file using that one-time pad.  Files require the pad to be decoded.

Next up is a demonstration of a frequency-based attack on the substitution cipher.
