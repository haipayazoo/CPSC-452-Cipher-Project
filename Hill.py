from CipherInterface import *
import math
from copy import copy, deepcopy

class Hill(CipherInterface):

	alphabet = "abcdefghijklmnopqrstuvwxyz"

	# BECAUSE THE TITAN SERVER DOES NOT HAVE NUMPY I HAVE BEEN FORCED
	# TO CREATE THE FOLLOWING FUNCTIONS

	# this specific implementation of the hill cipher uses 3 character
	# blocks and thus a 9 character string as a key.
	# "GYBNQKURP" is a valid key for testing

	# the key for a hill cipher must be an invertable matrix but the
	# validation of this is not implemented

	# Matrix Multiplication
	# takes in matrices a and b and returns the product
	def mMul(self, a, b):
		# init variables
		a_rows = len(a)
		a_cols = len(a[0])
		b_rows = len(b)
		b_cols = len(b[0])

		# number of columns in 'a' have the equal the number of rows in 'b'
		if(a_cols == b_rows):
			# create empty matrix
			c_rows = a_rows
			c_cols = b_cols
			c = []
			for rows in range(0, c_rows):
				c.append([])
				for cols in range(0, c_cols):
					c[rows].append(0)

			x = 0
			# iterate through rows
			for row in range(0, c_rows):
				# iterate through columns
				for col in range(0, c_cols):
					#add up the products of the corresponding indexs of the matrix
					total = 0
					for i in range(0, a_cols): # since a_cols = b_rows either can be used here
						total = total + (a[row][i] * b[i][col])
					c[row][col] = total
			return c
		else:
			print("mMul error" + str(a) + " * " + str(b))
			return []

	# Matrix Modulus
	# modulus each item in the matrix and return the result
	def mMod(self, matrix, mod):
		rows = len(matrix)
		cols = len(matrix[0])

		for row in range(0, rows):
			for col in range(0, cols):
				matrix[row][col] = matrix[row][col] % mod

		return matrix

	# Matrix remove row from matrix
	def mRmRow(self, matrix, row):
		del matrix[row]

	# Matrix remove column from matrix
	def mRmCol(self, matrix, col):
		rows = len(matrix)
		for row in range(0, rows):
			del matrix[row][col]

	# flip the matrix around the diagonal line
	def mTranspose(self, matrix):
		rows = len(matrix)
		cols = len(matrix[0])
		temp_matrix = deepcopy(matrix)

		for row in range(0, rows):
			for col in range(0, cols):
				matrix[row][col] = temp_matrix[col][row]

	# Matrix Determinant
	# returns the determinant of a matrix
	# only tested up to 3x3 unknown results for NxN matrix
	def mDet(self, matrix):
		rows = len(matrix)
		cols = len(matrix[0])

		if not rows == cols:
			print("Cannot find determinant of a non-square matrix")
			return []

		# if the matrix is 2x2 then return (ad - bc)
		if rows == 2:
			a = matrix[0][0]
			b = matrix[0][1]
			c = matrix[1][0]
			d = matrix[1][1]
			return (a * d) - (b * c)
		else:
			# if the matrix is larger than 2x2 then we need to reduce it to 2x2 chunks

			# use the formula on 'https://www.wikihow.com/Find-the-Inverse-of-a-3x3-Matrix'
			det = 0
			for col in range(0, cols):
				# create a clone of the matrix and remove the row and column that the current element belongs to
				sub_matrix = deepcopy(matrix)
				self.mRmRow(sub_matrix, 0)
				self.mRmCol(sub_matrix, col)

				# find the sub matrix's determinant
				sub_det = self.mDet(sub_matrix)
				posNeg = 1
				if col == 1:
					posNeg = -1
				det = det + (sub_det * matrix[0][col] * posNeg)

			return det

	# Create and return the adjugate matrix of a given matrix
	def mAdj(self, matrix):
		rows = len(matrix)
		cols = len(matrix[0])
		
		# create original adjugate matrix
		madj = [[1, -1, 1], [-1, 1, -1], [1, -1, 1]]

		# for each element of the matrix set the adjugate to the determinant of the 2x2 minor matrices
		for row in range(0, rows):
			for col in range(0, cols):
				# create sub matrix
				sub_matrix = deepcopy(matrix)
				self.mRmRow(sub_matrix, row)
				self.mRmCol(sub_matrix, col)

				# set the adj to the det of the sub matrix times the previous value
				madj[row][col] = madj[row][col] * self.mDet(sub_matrix)

		return madj

	# Matrix Inverse
	# returns an inverse of the original matrix if possible, otherwise empty array
	def mInv(self, matrix):
		rows = len(matrix)
		cols = len(matrix[0])

		# check that the determinant is not 0
		det = self.mDet(matrix)
		if det == 0:
			print("Inverse not possible")
			return []

		# transpose the matrix
		self.mTranspose(matrix)

		# create adjugate matrix
		madj = self.mAdj(matrix)

		# mod each value of the adj by the 26 and subtract that from 26
		for row in range(0, rows):
			for col in range(0, cols):
				matrix[row][col] = 26 - (madj[row][col] % 26)

		return matrix


	# returns a matrix (3x3) form of the key
	def translateKey(self):
		self.key = self.key.lower()
		c = 0
		k = []
		for row in range(0, 3):
			k.append([])
			for col in range(0, 3):
				k[row].append(self.alphabet.index(self.key[c]))
				c = c + 1
		return k

	# returns a matrix form of the text
	# the text is written down each column and additional columns are added if needed
	def translateTextToMatrix(self, plaintext):
		# matrix that will hold the plaintext
		mpt = []
		rows = 3
		cols = int(math.ceil(len(plaintext) / 3))

		# initialize the matrix
		for row in range(0, rows):
			mpt.append([])
			for col in range(0, cols):
				mpt[row].append(0)

		# a counter for which index we are at for the plaintext
		c = 0;

		#iterate through each column
		for col in range(0, cols):
			# iterate through each row
			for row in range(0, rows):
				# if we are still in the bounds of the plaintext just add the plaintext
				if c < len(plaintext):
					mpt[row][col] = self.alphabet.index(plaintext[c])
					c = c + 1
				else:
					# padding using only 'x' characters (not secure)
					mpt[row][col] = self.alphabet.index('x')

		return mpt

	# returns the text form of a given matrix
	def translateMatrixToText(self, matrix):
		text = ""
		rows = len(matrix)
		cols = len(matrix[0])

		# read the matrix column by column, top to bottom
		for col in range(0, cols):
			for row in range(0, rows):
				text = text + self.alphabet[matrix[row][col]]

		return text


	# Encrpyts the plaintext using the Railfence cipher
	def encrypt(self, plaintext):
		# matrix form of the key
		mk = self.translateKey()

		# matrix form of the plaintext
		mpt = self.translateTextToMatrix(plaintext)

		# the ciphertext is generated by multiplying the key by the plaintext
		mct = self.mMul(mk, mpt)

		# modulus each element by 26
		mct = self.mMod(mct, 26)

		ciphertext = self.translateMatrixToText(mct)

		return ciphertext

	# Decrypts the ciphertext using the Railfence cipher
	def decrypt(self, ciphertext):
		# matrix form of the key
		mk = self.translateKey()

		# inverse the key
		self.mInv(mk)

		# matrix form of the ciphertext
		mct = self.translateTextToMatrix(ciphertext)

		# the plaintext is generated by multiplay the key by the ciphertext
		mpt = self.mMul(mk, mct)

		# modulus each element by 26
		mpt = self.mMod(mpt, 26)

		# create plaintext
		plaintext = self.translateMatrixToText(mpt)

		# remove padding
		while plaintext[-1] == "x":
			plaintext = plaintext[:-1]

		return plaintext
