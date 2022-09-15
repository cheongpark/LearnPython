import requests

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
        "timestamp": "0bd098bc6c03b8508005383b70f623e9",
        "code": "0",
    },
    headers={
        "referer": "https://controlc.com/",
    }
)
 
print(response.text)

with open(
    "./test.html", 
    'w', 
    encoding='UTF-8'
) as f:
    f.write(response.text)