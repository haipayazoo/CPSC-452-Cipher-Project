import math
from CipherInterface import *


class Railfence(CipherInterface):

	# Encrpyts the plaintext using the Railfence cipher
	def encrypt(self, plaintext):
		rail = [['\n' for j in range(len(plaintext))] for i in range(int(self.key))]
		wrap = True
		row, col = 0, 0

		# Constructs the matrix from our plaintext
		for i in range(len(plaintext)):
			if(row == 0) or (row == int(self.key) - 1):
				wrap = not wrap

			rail[row][col] = plaintext[i]
			col += 1
			row += 1

			if wrap:
				row = 0

		result =[]

		# Gets the results from our matrix
		for i in range(int(self.key)):
			for j in range(len(plaintext)):
				if rail[i][j] != '\n':
					result.append(rail[i][j])

		return("" .join(result))

	# Decrypts the ciphertext using the Railfence cipher
	def decrypt(self, ciphertext):

			rail = [['\n' for j in range(len(ciphertext))] for i in range(int(self.key))]
			row, col = 0, 0
			result = []
			columns = math.ceil(len(ciphertext) / int(self.key))
			long_rows = len(ciphertext) % int(self.key)

			# Executes this if there are long rows in our matrix
			if(long_rows > 0):

				# Constructs the matrix
				for i in range(len(ciphertext)):
					rail[row][col] = ciphertext[i]

					col += 1

					if(col == columns):
						if(long_rows > 0):
							col %= columns
							long_rows -= 1

					if(col == columns - 1):
						if(long_rows <= 0):
							col %= columns - 1

					if(col == 0):
						row += 1
			# If there are no long rows in our matrix
			else:

				# Constructs the matrix
				for i in range(len(ciphertext)):
					rail[row][col] = ciphertext[i]

					col = (col + 1) % columns

					if(col == 0):
						row += 1

			# Gets the results from our constructed matrix
			for i in range(columns):
				for j in range(int(self.key)):
					if rail[j][i] != '\n':
						result.append(rail[j][i])

			return("".join(result))
