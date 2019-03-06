from CipherInterface import *
import math

class Vigenre(CipherInterface):

	def table_lookup(self, plain, key, reverse=False):
		pindex = ord(plain) - 97
		kindex = ord(key) - 97

		if not reverse:
			offset = (pindex + kindex) % 26
		else:
			offset = (pindex - kindex) % 26

		return chr(offset + 97)


	def encrypt(self, plaintext):
		self.key.replace(' ', '')

		ciphertext = ""

		# repeat the key enough to cover the plaintext
		length = math.ceil(len(plaintext) / len(self.key))
		keytext = self.key * length

		for p,k in zip(plaintext, keytext):
			ciphertext += self.table_lookup(p, k)

		return ciphertext

	def decrypt(self, ciphertext):
		self.key.replace(' ', '')

		plaintext = ""

		# repeat the key enough to cover the plaintext
		length = math.ceil(len(ciphertext) / len(self.key))
		keytext = self.key * length

		for p,k in zip(ciphertext, keytext):
			plaintext += self.table_lookup(p, k, reverse=True)

		return plaintext
