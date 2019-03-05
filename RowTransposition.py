from CipherInterface import *
import math

class RowTransposition(CipherInterface):
    
    def encrypt(self, plaintext):
        cols=len(self.key)
        rows=math.ceil(len(plaintext)/cols)
        padd=['x','y','z','a','b','c','d']
        x=0
        key=list(self.key)
        cyphertext=''
        while len(plaintext)<rows*cols:
            plaintext=plaintext+padd[x]
            x=(x+1)%len(padd)
        current=0
        matrix=[['' for j in range(cols)]for i in range(rows)]
        plainindex=0
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                matrix[r][c]=plaintext[plainindex]
                plainindex=plainindex+1
        for num in key:
            for row in matrix:
                cyphertext=cyphertext+row[int(num)-1]
        return cyphertext

    def decrypt(self, ciphertext):
        return "Decrypted text!"


#test code
#x=RowTransposition()
#x.setKey('3421567')
#print(x.encrypt('transpositionciphers'))
