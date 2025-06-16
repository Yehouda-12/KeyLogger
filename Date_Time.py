#קוד מייבא את מחלקת datetime(תאריך ושעה)
from datetime import datetime


#הקוד  שומר את התאריך והשעה הנוכחיים במשתנה כולל שניות וחלקי שניות, ומדפיס אותם למסך
now = datetime.now()
print(now)

# שומר רק שנה.חודש.יום.שעה.דקה ומדפיס אותם למסך
now = datetime.now().strftime("%Y-%m-%d %H:%M")#Y=year m=month d= day H=hour M=minut
print(now)
