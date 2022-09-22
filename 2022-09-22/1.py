import requests
from bs4 import BeautifulSoup

title = input("제목 : ")
text = input("내용 : ")

response = requests.post(
    "https://controlc.com/index.php",
    params = {
        "act" : "submit"
    },
    data = {
        "antispam": "1",
        "paste_title": title,
        "input_text": text,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "code": "0",
    },
    headers = {
        "referer": "https://controlc.com/",
    }
)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.select_one(selector = '#wrapper > div.rounded10.whiteBG.pad20 > div.successfull > div.input-copy > form > input[type=text]')

value = content['value']

print("제작된 주소 : " + value)

#제목 가져오기
getTitle = requests.get(
    value,
)

soup = BeautifulSoup(getTitle.text, 'html.parser')
title = soup.select_one(selector = '#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)')

print("확인용 제목 : " + title.get_text())

#타이틀 가져오기
content = soup.select_one(selector = '#pasteFrame')
titleSRC = content['src']

getContent = requests.get(
    titleSRC,
)

soup = BeautifulSoup(getContent.text, 'html.parser')
titleText = soup.select_one(selector = '#thepaste').text

print("확인용 텍스트 : " + titleText)