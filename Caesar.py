from CipherInterface import *

class Caesar(CipherInterface):

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	def encrypt(self, plaintext):
		#init cipher text
		ciphertext = ""

		#make the plaintext lowercase
		plaintext = plaintext.lower()

		#iterate through all characters in the plaintext
		for c in plaintext:
			#if the character is a letter then cipher it
			if c in self.alphabet:
				# get the index of the letter
				index = self.alphabet.index(c)

				# shift the index by the key
				index = index + int(self.key)

				#if the index goes past the length of the alphabet then wrap it around
				if index >= len(self.alphabet):
					index = index - len(self.alphabet)

				#append the cipher letter onto the cipher text
				ciphertext = ciphertext + self.alphabet[index]
			else:
				#if the character is not in the alphabet add a space
				ciphertext = ciphertext + " "

		return ciphertext

	def decrypt(self, ciphertext):
		#init plain text
		plaintext = ""

		#iterate through all characters in the ciphertext
		for c in ciphertext:
			#check that the character is in the alphabet
			if c in self.alphabet:
				#get the index of the cipher letter
				index = self.alphabet.index(c)

				#shift the index backwards by the key
				index = index - int(self.key)

				#wrap the index around if needed
				if index < 0:
					index = index + len(self.alphabet)

				#append the translated letter onto the plaintext
				plaintext = plaintext + self.alphabet[index]
			else:
				#if the character is not in the alphabet add a space
				plaintext = plaintext + " "

		return plaintext
