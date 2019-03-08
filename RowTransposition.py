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
        #initialize variables
        plaintext = ""

        len_key = len(self.key)
        len_ct = len(ciphertext)

        #calculate number of rows
        num_rows = int(len_ct / len_key)

        #create an array of rows
        rows = []

        #initialize rows to empty strings
        for x in range(0, num_rows):
            rows.append("")

        #copy the ciphertext into the rows by using the key to select what to concat first
        #for each number in the key, copy the corresponding column into the rows
        for column in range(1, len_key + 1):
            # get the index of the key at the column value
            # EX: key = 3421567 for column 1 will return 3 and then column 2 will return 2
            index = self.key.index(str(column))

            #find the point in the ciphertext where the column should start
            col_start = index * num_rows

            # for each row append the corresponding ciphertext characters offset at the index
            for row in range(0, num_rows):
                # concat onto the row the ciphertext at where the column should start plus the row offset
                rows[row] = rows[row] + ciphertext[col_start + row]

        #concat each row onto the plaintext
        for row in range(0, num_rows):
            plaintext = plaintext + rows[row]

        #return the plaintext
        return plaintext
