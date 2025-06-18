from cryptography.fernet import Fernet

# יצירת מפתח חדש
key = Fernet.generate_key()

# שמירת המפתח לקובץ
with open("encryption.key", "wb") as key_file:
    key_file.write(key)

print("🔐 מפתח חדש נוצר ונשמר כ־encryption.key")
