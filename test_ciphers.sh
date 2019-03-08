#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Testing Playfair Cipher (small.txt)"
CIPHER=PLF
KEY=security
FILE_IN=small.txt
FILE_ENC=plf_small_enc.txt
FILE_DEC=plf_small_dec.txt
./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }

echo "Testing Row Transposition Cipher (small.txt)"
CIPHER=RTS
KEY=3421567
FILE_IN=small.txt
FILE_ENC=rts_small_enc.txt
FILE_DEC=rts_small_dec.txt
./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }

echo "Testing Railfence Cipher (small.txt)"
CIPHER=RFC
KEY=3
FILE_IN=small.txt
FILE_ENC=rfc_small_enc.txt
FILE_DEC=rfc_small_dec.txt
./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }

echo "Testing Vigenere Cipher (small.txt)"
CIPHER=VIG
KEY=deceptive
FILE_IN=small.txt
FILE_ENC=vig_small_enc.txt
FILE_DEC=vig_small_dec.txt
./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }

echo "Testing Caesar Cipher (small.txt)"
CIPHER=CES
KEY=5
FILE_IN=small.txt
FILE_ENC=ces_small_enc.txt
FILE_DEC=ces_small_dec.txt
./cipher.py $CIPHER $KEY ENC $FILE_IN $FILE_ENC
./cipher.py $CIPHER $KEY DEC $FILE_ENC $FILE_DEC
cmp --silent $FILE_IN $FILE_DEC && { echo -e "$CIPHER ($FILE_IN): ${GREEN}SUCCESS${NC}"; rm $FILE_ENC; rm $FILE_DEC; } || { echo -e "$CIPHER ($FILE_IN): ${RED}FAILURE${NC}: check $FILE_IN, $FILE_ENC and $FILE_DEC for errors"; }