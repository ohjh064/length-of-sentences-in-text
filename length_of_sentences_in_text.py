import os
import sys
import re

sys.stdout =open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2019-11-수능-문장-영어-전처리.txt", "w", encoding="utf-8")

with open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2019-11-수능-문장-영어.txt","r", encoding="UTF-8") as file:
    lines = file.readlines()
    for line in lines:
        a = line.replace(" ","")
        b = a.strip("\n")
        print(str(b), end = "")

sys.stdout.close()

#as

sys.stdout =open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2019-11-수능-문장-영어.csv", "w", encoding="utf-8")

with open("C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2019-11-수능-문장-영어-전처리.txt","r", encoding="UTF-8") as file2:
    datas = file2.readlines()
    for data in datas:
        a = re.split('[?.!]', data)
        for i in a:
            b = re.sub('[^a-zA-Z0-9]','',i).strip()
            print(str(len(b)) + "," +"".join(b), end = "\n")

sys.stdout.close()