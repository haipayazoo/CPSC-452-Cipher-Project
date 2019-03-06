class CipherInterface:

	def __init__(self):
		self.key = ""

	def setKey(self, key):
		self.key = key

	def encrypt(self, plaintext):
		print("encrypt!")

	def decrypt(self, ciphertext):
		print("decrypt!")
