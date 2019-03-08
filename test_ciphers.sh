#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

CIPHERS=( PLF RTS RFC VIG CES )
KEYS=( security 3421567 3 deceptive 5 )

echo "##### small.txt #####"
FILE_IN=small.txt
for c in {0..4}
do
	CIPHER=${CIPHERS[c]}
	KEY=${KEYS[c]}
	FILE_ENC=${CIPHER}_small_enc.txt
	FILE_DEC=${CIPHER}_small_dec.txt
	echo "Testing $CIPHER Cipher (${FILE_IN})"
	./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
	./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
	sed -i -e '$a\' $FILE_DEC # add a newline onto the end of the decrypted file
	cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }
done

echo ""
echo ""
echo "##### big.txt #####"
FILE_IN=big.txt
for c in {0..4}
do
	CIPHER=${CIPHERS[c]}
	KEY=${KEYS[c]}
	FILE_ENC=${CIPHER}_big_enc.txt
	FILE_DEC=${CIPHER}_big_dec.txt
	echo "Testing $CIPHER Cipher (${FILE_IN})"
	./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
	./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
	cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }
done