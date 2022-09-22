import requests
from bs4 import BeautifulSoup

for i in range(108):
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
            'block': i,
            'addr1': '서울',
            'sort': '13D',
        },
        headers = {
            'Referer': 'https://auction.realestate.daum.net/v15/',
        }
    )

    # with open("./test.html", 'w', encoding='UTF-8') as f:
    #     f.write(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    trs = soup.select(selector = '#frm_myreg > table > tbody > tr')

    for tr in trs:
        print(tr.select_one('td.no_bdL_check_new a').text)
