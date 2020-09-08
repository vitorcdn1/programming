from cryptography.fernet import Fernet
from os import getcwd, system

system("clear")
print(getcwd())

def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
                key_file.write(key)

def load_key():

        return open("key.key", "rb").read()

write_key()
key = load_key()

message = "Olá mundo".encode()

f = Fernet(key)

encrypted = f.encrypt(message)
decrypt = f.decrypt(encrypted)


print(encrypted)
print(decrypt.decode())