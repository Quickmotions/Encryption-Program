# Encryption-Program
Simple to use module/stand-alone program

features:
encryption,
decrytion,
key generation,
key storage,
using cryptography python package,

This program can be run on its own to encrypt files or text from user or used as a module in a greater program allowing it to decrypt and encrypt files and information when 
called upon.

also works with basically any file type including: zipped folders, gif, jpg, svg, mp3, txt, ect.

--------

from EncryptModule import generate_key, encrypt_message, decrypt_message, main

the encryption and decryption functions require two inputs:
-data which has been encoded (using data.encode() only if it is a string)
and a key which is also encoded (using key.encode() if it is a string)

generate_key() requires a file name (eg. keyfile.key)

(The program can generate you a new key by using the function generate_key())

--------
Inside the repository is an example key and the actual python code but encrypted
you can use the program to decrypt this file using the example key to see how it shows the code again.


