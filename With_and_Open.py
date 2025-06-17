#פותח קובץ .txt
open_txt=open("name of file.txt", "a")
#כותב ב.txt
open_txt.write("hello")
# צריך לסגור אם לא זה יכול לעשות בעיות
open_txt.close()

with open("name of file ", "a") as f:
    f.write("Hello\n")
git
