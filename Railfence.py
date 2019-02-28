from CipherInterface import *

class Railfence(CipherInterface):

	def encrypt(self, plaintext):
		return "Encrypted text!\n"

	def decrypt(self, ciphertext):
		return "Decrypted text!"
