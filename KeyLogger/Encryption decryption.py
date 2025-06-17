from cryptography.fernet import Fernet

# טען את המפתח
with open("encryption.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

# פתח את הקובץ המוצפן
with open("keylogger.txt", "rb") as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                decrypted = fernet.decrypt(line)
                print(decrypted.decode())
            except Exception as e:
                print("[שגיאת פענוח]", e)
