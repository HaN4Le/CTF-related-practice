import os
import re
from bs4 import BeautifulSoup

path = "F:\新建文件夹"

files = os.listdir(path)

for f in files:
    if re.search('\.html$', f):
        soup = BeautifulSoup(open(f,'r', encoding = "utf-8"),"lxml")
        text = soup.get_text()
        print(text)
        print(type(text))
