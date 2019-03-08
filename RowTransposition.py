from CipherInterface import *
import math

class RowTransposition(CipherInterface):

    def encrypt(self, plaintext):
        cols = len(self.key)
        rows = math.ceil(len(plaintext)/cols)
        padd = ['x','y','z','a','b','c','d']
        x = 0
        key = list(self.key)
        cyphertext = ''

        while len(plaintext) < rows * cols:
            plaintext = plaintext + padd[x]
            x = (x + 1) % len(padd)

        index = 0
        matrix = [['' for j in range(cols)]for i in range(rows)]
        plainindex = 0

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                matrix[r][c] = plaintext[plainindex]
                plainindex = plainindex + 1

        for num in key:
            for row in matrix:
                cyphertext = cyphertext + row[int(num) - 1]

        return cyphertext

    def decrypt(self, ciphertext):
        key = self.key
        padd = ['x','y','z','a','b','c','d']
        key_length = len(key)

        plaintext = ''
        rows = len(ciphertext)/key_length
        index = 0

        while index < rows:
            x = 1

            while x < key_length + 1:
                index = int((rows * (key.index(str(x)))) + index)
                plaintext = plaintext + ciphertext[index]
                x += 1

            index += 1
            x -= 1
            while plaintext[-1:] in padd:
                plaintext = plaintext[:-1]

        return plaintext
