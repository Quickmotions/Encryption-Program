# Encryption-Program
Simple to use module/stand-alone program

features:
-encryption
-decrytion
-key generation
-key storage

This program can be run on its own to encrypt files or text from user or used as a module in a greater program allowing it to decrypt and encrypt files and information when 
called upon.

To use as a module just:
from EncryptModule import generate_key, encrypt_message, decrypt_message, main

the encryption and decryption functions require two inputs:
-data which has been encoded (using data = data.encode() only if it is a string)
-a key which is also encoded.

the program can generate you a new key by using the function generate_key()

