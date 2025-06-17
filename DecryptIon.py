from cryptography.fernet import Fernet

# Charger la clé
def decryption():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    # Lire et déchiffrer chaque ligne
    with open("log_encrypted.txt", "rb") as f:
        for line in f:
            decrypted = cipher.decrypt(line.strip())
            print(decrypted.decode())
