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
        key = self.key
        padd=['x','y','z','a','b','c','d']
        lenk=len(key)
       
        plaintext=''
        rows=len(ciphertext)/lenk
        current=0
        
        while current < rows:
            x=1
            while x< lenk+1:
                index=int((rows*(key.index(str(x))))+current)
                plaintext=plaintext+ciphertext[index]
                x=x+1
            current=current+1
            x=-1
            while plaintext[-1:] in padd:
                plaintext=plaintext[:-1]
        return plaintext


#test code
# x=RowTransposition()
# x.setKey('3421567')
# encrypted=x.encrypt('transpositionciphers')
# print(encrypted)
# print(x.decrypt(encrypted))
