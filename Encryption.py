from cryptography.fernet import Fernet

# מייצר מפתח
key = Fernet.generate_key()

# שומר את המפתח בקובץ"secret.key"
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("מפתח  מיוצר ונשמר בהצלחה")
