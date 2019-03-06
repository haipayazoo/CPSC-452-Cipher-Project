class CipherInterface:

	def __init__(self):
		self.key = ""

	def setKey(self, key):
		self.key = key

	def encrypt(self, plaintext):
		print("encrypt!")

	def decrypt(self, ciphertext):
		print("decrypt!")

	def remove_space(self, plaintext):
		plaintext = plaintext.replace('\n', "")
		plaintext = plaintext.replace('\t', "")
		plaintext = plaintext.replace(" ", "")
		return plaintext;
