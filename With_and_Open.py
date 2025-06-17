from datetime import datetime
import time
while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")#Y=year m=month d= day H=hour M=minut


#פותח קובץ .txt
    with open("name of file ", "a",encoding="utf-8") as f:
        f.write(now +"\n")

    time.sleep(60)