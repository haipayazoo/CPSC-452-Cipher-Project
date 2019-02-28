#! python3

import sys

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
help_log = "CPSC 452 Cipher Project\n\nUsage: ./cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>\n\nCIPHER NAME:\n\tPLF - Playfair Cipher\n\tRTS - Row Transposition Cipher\n\tRFC - Railfence Cipher\n\tVIG - Vigenre Cipher\n\tCES - Caesar Cipher\n\tMAC - Monoalphabetic Cipher\n\nKEY:\n\tThe key to use in either encryption or decryption\n\nENC/DEC:\n\tENC - Encrypt\n\tDEC - Decrypt\n\nINPUT FILE:\n\tThe file to encrypt/ decrypt\n\nOUTPUT FILE:\n\tThe file to store the output of the encryption/ decryption"

cipher = CipherInterface()
cipher_name = "";
key = "";
mode = "";
input_file_name = "";
output_file_name = "";

def handleHelp():
	# check for the '--help' tag and print the help log
	if(len(sys.argv) > 1):
		if(sys.argv[1] == "--help"):
			print(help_log)
			exit()

def checkCommandLineArgs():
	# make sure that all of the inputs are expected
	assert (len(sys.argv) == 6), "Wrong number of command line arguments. see --help"
	assert (sys.argv[1] in valid_ciphers), "Not a recognized cipher. see --help"
	assert (sys.argv[3] in ["ENC", "DEC"]), "Invalid function <ENC/DEC>. see --help"

def parseArgs():
	# makes sure we can access global vars
	global cipher_name
	global key
	global mode
	global input_file_name
	global output_file_name

	# move the arguments into the global variables
	cipher_name = sys.argv[1];
	key = sys.argv[2];
	mode = sys.argv[3];
	input_file_name = sys.argv[4];
	output_file_name = sys.argv[5];

def initCipher():
	# make sure we can access the cipher
	global cipher

	# set cipher to specified cipher
	if(cipher_name == "PLF"):
		cipher = Playfair();
	elif(cipher_name == "RTS"):
		cipher = RowTransposition();
	elif(cipher_name == "RFC"):
		cipher = Railfence();
	elif(cipher_name == "VIG"):
		cipher = Vigenre();
	elif(cipher_name == "CES"):
		cipher = Caesar();
	elif(cipher_name == "MAC"):
		cipher = Monoalphabetic();

	# set cipher key
	cipher.setKey(key)

def execute():
	# set up input and output files
	inputFile = open(input_file_name, "r");
	outputFile = open(output_file_name, "w");

	# execute the encrypt/ decrypt
	if(mode == "ENC"):
		outputFile.write(cipher.encrypt(inputFile.read()));
	elif(mode == "DEC"):
		outputFile.write(cipher.decrypt(inputFile.read()));


def main():
	handleHelp();
	checkCommandLineArgs();
	parseArgs();
	initCipher();
	execute();

main()