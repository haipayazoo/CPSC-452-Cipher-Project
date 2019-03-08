from CipherInterface import *

class Playfair(CipherInterface):

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphabetNoJ = "abcdefghiklmnopqrstuvwxyz"

	def __init__(self):
		CipherInterface.__init__(self)

	# adds the key to the matrix and fills the rest with the alphabet
	# WARNING:
	def buildMatrix(self):
		matrix =   [['', '', '', '', ''],
					['', '', '', '', ''],
					['', '', '', '', ''],
					['', '', '', '', ''],
					['', '', '', '', '']]

		# add key to the matrix
		x = 0
		y = 0
		for c in self.key:
			#filter out non-alphabetic characters
			if c in self.alphabetNoJ:
				if c == 'j':#all 'j' will be treated as 'i'
					c = 'i';
				#make sure no duplicate get in
				if not any(c in sub_matrix for sub_matrix in matrix):
					#set character in matrix
					matrix[y][x] = c

					#increment
					x = x + 1
					if x > 4:
						x = 0
						y = y + 1

		# fill matrix with the rest of the alphabet
		for c in self.alphabetNoJ: # alphabet without 'j'
			# make sure no duplicate characters get in
			if not any(c in sub_matrix for sub_matrix in matrix):
				#set character in matrix
				matrix[y][x] = c

				#increment
				x = x + 1
				if x > 4:
					x = 0
					y = y + 1

		return matrix

	#translate a playfair block through a playfair matrix
	#inputing 'ENC' into the mode will put it in encrypt mode, else is decrypt
	def translateBlock(self, block, matrix, mode):
		b1x = 0
		b1y = 0
		b2x = 0
		b2y = 0

		cipher_block = ['', '']

		#generate x and y coordinates for each character in the block
		y = 0
		for sub_matrix in matrix:
			if block[0] in sub_matrix:
				b1x = sub_matrix.index(block[0])
				b1y = y
			if block[1] in sub_matrix:
				b2x = sub_matrix.index(block[1])
				b2y = y

			y = y + 1

		if b1x == b2x: # same column
			#cipher block becomes the letters in the matrix below the plaintext block
			if mode == "ENC":
				new_b1y = b1y + 1
				new_b2y = b2y + 1
			else:# DEC
				new_b1y = b1y - 1
				new_b2y = b2y - 1

			# wrap around the matrix if it goes out of bounds
			if new_b1y > 4:
				new_b1y = 0
			if new_b2y > 4:
				new_b2y = 0
			if new_b1y < 0:
				new_b1y = 4
			if new_b2y < 0:
				new_b2y = 4

			#set the cipher block
			cipher_block[0] = matrix[new_b1y][b1x]
			cipher_block[1] = matrix[new_b2y][b2x]
		elif b1y == b2y: # same row
			#cipher block becomes the letter to the right of the letter in the origin block
			if mode == "ENC":
				new_b1x = b1x + 1
				new_b2x = b2x + 1
			else: # DEC
				new_b1x = b1x - 1
				new_b2x = b2x - 1

			# wrap around the matrix if it goes out of bounds
			if new_b1x > 4:
				new_b1x = 0
			if new_b2x > 4:
				new_b2x = 0
			if new_b1x < 0:
				new_b1x = 4
			if new_b2x < 0:
				new_b2x = 4

			#set the cipher block
			cipher_block[0] = matrix[b1y][new_b1x]
			cipher_block[1] = matrix[b2y][new_b2x]
		else:
			#translate
			cipher_block[0] = matrix[b1y][b2x]
			cipher_block[1] = matrix[b2y][b1x]

		return cipher_block

	#create two character blocks from the plaintext
	#also inserts 'x' where the same character is in the same block
	def createBlocks(self, plaintext):
		blocks = []

		#looping through all the characters of the plaintext
		x = 0
		while x < len(plaintext):
			#initialize the block
			block = ['', '']

			#fill the two characters in the block
			while block[1] == '':# while the block is not complete
				if x >= len(plaintext):# if we are still looking for a character to complete a block but we are past the end of the plaintext we fill c2 with 'x'
					block[1] = 'x'
					break

				if plaintext[x] in self.alphabet:#check the character is in the alphabet
					if block[0] == '':# if the first character is empty, fill it
						block[0] = plaintext[x]
						#increment
						x = x + 1
					elif block[0] == plaintext[x]:# if the first character is the same as the new character fill in an x
						block[1] = 'x'
						# do not increment because we did not use the character at plaintext[x]
					else:
						block[1] = plaintext[x]
						#increment
						x = x + 1
				else:
					# if the character is not in the alphabet go to the next character
					x = x + 1

			if not block[0] == '':# if it is not an empty block. append it
				#append block to list of blocks to return
				blocks.append(block)

		return blocks


	def encrypt(self, plaintext):
		# build matrix
		matrix = self.buildMatrix()

		#create blocks from the plaintext
		plaintext_blocks = self.createBlocks(plaintext)

		# build ciphertext
		ciphertext = ""
		for plaintext_block in plaintext_blocks:
			#translate the plaintext block
			cipher_block = self.translateBlock(plaintext_block, matrix, "ENC")

			#append block to ciphertext
			ciphertext = ciphertext + cipher_block[0]
			ciphertext = ciphertext + cipher_block[1]

		return ciphertext

	def decrypt(self, ciphertext):
		#build matrix
		matrix = self.buildMatrix()

		#create blocks from ciphertext
		cipher_blocks = self.createBlocks(ciphertext)

		# build plaintext
		plaintext = ""
		for cipher_block in cipher_blocks:
			#translate the plaintext block
			plaintext_block = self.translateBlock(cipher_block, matrix, "DEC")

			#append block to plaintext
			if plaintext_block[1] == 'x':
				plaintext = plaintext + plaintext_block[0]
			else:
				plaintext = plaintext + plaintext_block[0]
				plaintext = plaintext + plaintext_block[1]

		# remove the x that can be appended to the end of the plaintext
		if plaintext[len(plaintext) - 1] == 'x':
			plaintext = plaintext[:-1]

		return plaintext
