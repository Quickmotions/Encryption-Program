
def generate_key(file_name):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_message(data, key):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    encrypted_message = f.encrypt(data)

    return encrypted_message , key

def decrypt_message(data, key):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    decrypted_message = f.decrypt(data)
    return decrypted_message, key

def main():
    if (input("Type '1' for file or '2' for string: ") == "1"):
       file_name = input("Enter file name (eg: file.txt...): ")
       data = open(file_name, "rb").read()
    else:
        data = input("Type string: ").encode()
    choice = input("Type '1' to generate a key or '2' to use a existing key from file or '3' to enter a key via text: ")
    if choice == "1":
        key_file = input("Type name of file for key:")
        key_file += ".key"
        key = generate_key(key_file)
    elif choice == "2":
        file_name = input("Enter the name of the key file: ")
        file_name += ".key"
        key = open(file_name, "rb").read()
    else: 
        key = input("Enter the 32 bit key: ")
    if(input("Type '1' for encryption or '2' for decryption: ") == "1"):
        message, key = encrypt_message(data, key) 
    else:
        message, key = decrypt_message(data, key)
    print("key:       "+ str(key))
    print("message:   "+ str(message))
    file_name = input("Enter the name of the new file: ")
    file_name += ".txt"
    with open(file_name, "wb") as message_file:
        message_file.write(message)
    exit()
if __name__ == '__main__':
    main()