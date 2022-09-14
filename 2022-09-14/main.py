import requests
import re

title = input("제목 : ")
text = input("내용 : ")

response = requests.post(
    "https://controlc.com/index.php?",
    params={
        "act" : "submit"
    },
    data={
        "subdomain": "",
        "antispam": "1",
        "website": "",
        "paste_title": title,
        "input_text": text,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": "",
        "code": "0",
    },
    headers={
        "referer": "https://controlc.com/",
    }
)

print(response.text)

with open(
    "C:/Users/user/Desktop/2022-09-14/test.html", 
    'w', 
    encoding='UTF-8'
) as f:
    f.write(response.text)