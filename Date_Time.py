from datetime import datetime


#הקוד מייבא את מחלקת datetime, שומר את התאריך והשעה הנוכחיים במשתנה, ומדפיס אותם למסך.
now = datetime.now()
print(now)

#שומר רק שנה.חודש.יום.שעה.דקה
now = datetime.now().strftime("%Y-%m-%d %H:%M")
print(now)