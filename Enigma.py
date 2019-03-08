from CipherInterface import *
import math

# The enigma cipher in this implementation takes in a key that is 26x3 characters lone
# this is then translated into 26 character keys for each rotor
# each rotor key should only contain 1 of each character in the alphabet

# the rotor will translate a single character across its key

# the enigma class will create 3 instances of the rotor and translate each
# character of plaintext across each rotor in order to encrypt and backwards
# to decrypt

class Rotor(CipherInterface):

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	def __init__(self):
		CipherInterface.__init__(self)
		self.position = 0
		self.array_in = []
		self.array_out = []

	def setKey(self, key):
		self.key = key

		for i in range(0, 26):
			self.array_in.append(i)
			self.array_out.append(self.key.index(self.alphabet[i]))

	# sets the position to the index of the char
	def setPos(self, posChar):
		self.position = self.alphabet.index(posChar)

	# encrypts 1 character at a time
	def encrypt(self, plaintext):
		# set the location input to the index of the letter plus the rotation
		loc_in = self.alphabet.index(plaintext) + self.position
		if loc_in > 25:
			loc_in = loc_in - 26

		# set the location output of the rotor to the index of the input plus the position
		loc_out = self.array_out.index(loc_in) + self.position
		if loc_out > 25:
			loc_out = loc_out - 26

		# set the ciphertext to the letter at the location out
		ciphertext = self.alphabet[loc_out]

		return ciphertext

	# decrypt 1 character at a time
	def decrypt(self, ciphertext):
		# set the location out side
		loc_out = self.alphabet.index(ciphertext) - self.position
		if loc_out > 25:
			loc_out = loc_out - 26

		loc_in = self.array_out[loc_out] - self.position
		if loc_in > 25:
			loc_in = loc_in - 26

		plaintext = self.alphabet[loc_in]

		return plaintext

	# rotate the rotor
	# if the rotation makes a full circle then return true, else return false
	def rotate(self):
		# rotate the rotor
		self.position = self.position + 1
		if self.position > 25:
			self.position = 0
			return True
		else:
			return False



class Enigma(CipherInterface):

	# this implementation of the Enigma Cipher assumes a start place of A A A
	# on all of the roters

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	rotors = []

	def setKey(self, key):
		self.key = key

		# create the list of rotors
		self.rotors.append(Rotor())
		self.rotors.append(Rotor())
		self.rotors.append(Rotor())

		# static rotor keys
		self.rotors[0].setKey("dkvqfibjwpescxhtmyauolrgzn")
		self.rotors[1].setKey("uolqfdkvescxhzntmyaibjwprg")
		self.rotors[2].setKey("lrescxgzndkvqfimyauobjwpht")

		# set the starting position of the rotors to that of the key
		self.rotors[0].setPos(self.key[:1])
		self.rotors[1].setPos(self.key[1:2])
		self.rotors[2].setPos(self.key[2:3])

	# Encrpyts the plaintext using the Railfence cipher
	def encrypt(self, plaintext):
		ciphertext = ""

		# for each character in the plaintext
		for c in plaintext:
			# if its a space
			if c == " ":
				# append a space
				ciphertext = ciphertext + c
			else:
				# if its not a space
				# encrypt the character on each roter
				for r in range(0, len(self.rotors)):
					c = self.rotors[r].encrypt(c)

				# rotate the rotors
				for r in range(0, len(self.rotors)):
					# if the rotor does not make a full rotation dont rotate the next rotor
					if not self.rotors[r].rotate():
						break

				ciphertext = ciphertext + c

		return ciphertext

	# Decrypts the ciphertext using the Railfence cipher
	def decrypt(self, ciphertext):
		plaintext = ""

		# for each character in the ciphertext
		for c in ciphertext:
			# if its a space
			if c == " ":
				# append a space
				plaintext = plaintext + c
			else:
				# if its not a space
				# decrypt the character on each rotor in reverse
				for r in range(0, len(self.rotors)):
					c = self.rotors[len(self.rotors) - r - 1].decrypt(c)

				# rotate the rotors
				for r in range(0, len(self.rotors)):
					# if the rotor does not make a full rotation dont rotate the next rotor
					if not self.rotors[r].rotate():
						break

				plaintext = plaintext + c

		return plaintext
