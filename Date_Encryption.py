from datetime import datetime
import time
from cryptography.fernet import Fernet
import os

# טעינת המפתח מהקובץ
def date_encryption():
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    cipher = Fernet(key)

    # לולאה אינסופית: כתיבה כל דקה
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Chiffrement
        encrypted_data = cipher.encrypt(now.encode())

        # כתיבה לקובץ מוצפן
        with open("log_encrypted.txt", "ab") as f:
            f.write(encrypted_data + b"\n")  # b"\n" = saut de ligne en binaire

        print(f"[✓] Heure enregistrée et chiffrée : {now}")

        # המתנה של דקה
        time.sleep(60)
