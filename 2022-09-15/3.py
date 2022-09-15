import requests
from bs4 import BeautifulSoup

with open("./test.html", 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
content = soup.select_one(selector='#wrapper > div.rounded10.whiteBG.pad20 > div.successfull > div.input-copy > form > input[type=text]')

value = content['value']

#타이틀 가져오기

html2 = requests.get(
    value,
)

toSoup = BeautifulSoup(html2.text, 'html.parser')
toTitle = toSoup.select_one(selector='#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)')

print("확인용 제목 : " + toTitle.get_text())