import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

response = requests.post(
        'https://auction.realestate.daum.net/ajax/main_list.php',
    params = {
        'addr1': '서울',
        'result': 99,
        'yongdo': 99,
        'yongdo_detail': 99,
        'sort': '13D',
    },
    data = {
        'block': 2,
        'addr1': '서울',
        'sort': '13D',
    },
    headers = {
        'Referer': 'https://auction.realestate.daum.net/v15/',
    }
)

with open("./test.html", 'w', encoding='utf-8') as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
trs = soup.select(selector = '#frm_myreg > table > tbody > tr')

datas = []
for tr in trs:
    data = {
        '사건번호': (tr.select_one('td.no_bdL_check_new a').text),
        #'': (tr.select_one('td.bottom9_new > div.ac_photo > a > img').text),
        '물건용도': (tr.select_one('td.bottom9_new > div.ac_box > a > p.used').text),
        '소재지': (tr.select_one('td.bottom9_new > div.ac_box > a > p.address').text),
        '감정': (tr.select_one('td.price_new > div.mapList_price.price_icon1 > p').text),
        '최저': (tr.select_one('td.price_new > div.mapList_price.price_icon2 > p').text),
        '시세': (tr.select_one('td.price_new > div.price_icon3_1').text),
        #'': (tr.select_one('td.price_new > div.mapList_price.price_icon3 > span').text)
        '진행확인': (tr.select_one('td.auctioned_new > div > p:nth-child(1) > span').text),
        #'': (tr.select_one('td.auctioned_new > div > p:nth-child(3) > span').text)
        '연락처': (tr.select_one('td.bottom9_new > div.ac_box > p.unusual > span.franchise').text)
    }
    datas.append(data)

with open('./main.json', 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(datas, ensure_ascii = False))
