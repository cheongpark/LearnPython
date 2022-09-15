from bs4 import BeautifulSoup

with open("./test.html", 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one(selector='#wrapper > div.rounded10.whiteBG.pad20 > div.successfull > div.input-copy > form > input[type=text]')

print(title['value'])