#!/usr/bin/env python3

import sys
import argparse

from CipherInterface import *
from Playfair import *
from RowTransposition import *
from Railfence import *
from Vigenre import *
from Caesar import *
from Monoalphabetic import *

# PLF - playfair cipher
# RTS - row transposition cipher
# RFC - railfence cipher
# VIG - vigenre cipher
# CES - caesar cipher
# MAC - monoalphabetic cipher

valid_ciphers = ["PLF", "RTS", "RFC", "VIG", "CES", "MAC"]

# Create our argument parser object
parser = argparse.ArgumentParser(description='Encrypt and decrypt using six different ciphers.', formatter_class=argparse.RawTextHelpFormatter)

# Add our arguments to the parser
parser.add_argument("cipher", help="""Name of the cipher to use. One of:
	PLF - Playfair
	RTS - Row Transposition
	RFC - Railfence
	VIG - Vigenere
	CES - Caesar
	MAC - Monoalphabetic""")

parser.add_argument("key", help="The key to use for encryption/decryption")
parser.add_argument("mode", help="Run the cipher in ENC (encryption) or DEC (decryption) mode")
parser.add_argument("input", help="The path to the input file")
parser.add_argument("output", help="The path to the output file")

# Make sure we have enough arguments, if not print the help message
if len(sys.argv) < 5:
	parser.print_help()
	sys.exit(1)

# Actually parse the arguments
arguments = parser.parse_args()


cipher = CipherInterface()

assert arguments.cipher in valid_ciphers, "Cipher not recognized. Use --help for more info."

# set cipher to specified cipher
if(arguments.cipher == "PLF"):
	cipher = Playfair()
elif(arguments.cipher == "RTS"):
	cipher = RowTransposition()
elif(arguments.cipher == "RFC"):
	cipher = Railfence()
elif(arguments.cipher == "VIG"):
	cipher = Vigenre()
elif(arguments.cipher == "CES"):
	cipher = Caesar()
elif(arguments.cipher == "MAC"):
	cipher = Monoalphabetic()

# Normalize and set the cipher key
if arguments.cipher in ["VIG", "PLF"]:
	normalizedKey = ""
	for char in str(arguments.key).lower():
		if 96 < ord(char) < 123:
			normalizedKey += char
	assert len(normalizedKey) > 0, "Zero length input key"
elif arguments.cipher in ["RFC", "CES"]:
	normalizedKey = int(arguments.key)
else:
	normalizedKey = str(arguments.key)
	assert normalizedKey, "Invalid key"

cipher.setKey(normalizedKey)

# set up input and output files
inputFile = open(arguments.input, "r")
outputFile = open(arguments.output, "w")

# Normalize the input file by stripping all non-lowercase ascii
rawInput = inputFile.read().lower()
normalizedInput = ""
for char in rawInput:
	if 96 < ord(char) < 123:
		normalizedInput += char

# Perform the encryption/decryption
if(arguments.mode == "ENC"):
	outputFile.write(cipher.encrypt(normalizedInput))
else:
	outputFile.write(cipher.decrypt(normalizedInput) + '\n')
