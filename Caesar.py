from CipherInterface import *

class Caesar(CipherInterface):

	def encrypt(self, plaintext):
		return "Encrypted text!\n"

	def decrypt(self, ciphertext):
		return "Decrypted text!"
