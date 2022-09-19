import requests
from bs4 import BeautifulSoup

title = input("제목 : ")
text = input("내용 : ")

response = requests.post(
    "https://controlc.com/index.php?",
    params={
        "act" : "submit"
    },
    data={
        "antispam": "1",
        "paste_title": title,
        "input_text": text,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "code": "0",
    },
    headers={
        "referer": "https://controlc.com/",
    }
)

with open(
    "./test.html", 
    'w', 
    encoding='UTF-8'
) as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.select_one(selector='#wrapper > div.rounded10.whiteBG.pad20 > div.successfull > div.input-copy > form > input[type=text]')

value = content['value']

print("제작된 주소 : " + value)

#타이틀 가져오기
html2 = requests.get(
    value,
)

toSoup = BeautifulSoup(html2.text, 'html.parser')
toTitle = toSoup.select_one(selector='#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)')

print("확인용 제목 : " + toTitle.get_text())