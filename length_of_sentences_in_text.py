import os
import sys
import re

sys.stdout =open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\19-21_수능_문장_영어_전처리.txt", "w", encoding="utf-8")

with open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\19-21_수능_문장_영어.txt","r", encoding="UTF-8") as file:
    lines = file.readlines()
    for line in lines:
        a = line.replace(" ","")
        b = a.strip("\n")
        print(str(b), end = "")

sys.stdout.close()

#as

sys.stdout =open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\19-21_수능_문장_영어_문장길이.csv", "w", encoding="utf-8")

with open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\19-21_수능_문장_영어_전처리.txt","r", encoding="UTF-8") as file2:
    datas = file2.readlines()
    for data in datas:
        a = re.split('[?.!]', data)
        for i in a:
            b = [j for j in i if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+",j)]
            print(str(len(b)) + "," +"".join(b), end = "\n")

sys.stdout.close()