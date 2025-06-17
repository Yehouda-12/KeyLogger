from cryptography.fernet import Fernet

with open("encryption.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

with open("keylogger.txt", "rb") as f:
    for line in f:
        decrypted = fernet.decrypt(line.strip())
        print(decrypted.decode())