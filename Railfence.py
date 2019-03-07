import math
from CipherInterface import *


class Railfence(CipherInterface):

	def encrypt(self, plaintext):
		rail = [['\n' for j in range(len(plaintext))] for i in range(int(self.key))]
		wrap = True
		row, col = 0, 0

		for i in range(len(plaintext)):
			if(row == 0) or (row == int(self.key) - 1):
				wrap = not wrap

			rail[row][col] = plaintext[i]
			col += 1
			row += 1

			if wrap:
				row = 0

		result =[]

		for i in range(int(self.key)):
			for j in range(len(plaintext)):
				if rail[i][j] != '\n':
					result.append(rail[i][j])

		return("" .join(result))

	def decrypt(self, ciphertext):

			rail = [['\n' for j in range(len(ciphertext))] for i in range(int(self.key))]
			row, col = 0, 0
			result = []
			columns = math.ceil(len(ciphertext) / int(self.key))
			long_rows = len(ciphertext) % int(self.key)

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

			for i in range(columns):
				for j in range(int(self.key)):
					if rail[j][i] != '\n':
						result.append(rail[j][i])

			return("".join(result))
