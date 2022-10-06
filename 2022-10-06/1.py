import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time #서버에서 비정상적 판단때문에 넣는 것 타임을 줌

count = 1
datas = []
citys = {"서울", "인천", "대구", "울산", "세종", "충남", "경북", "전북", "제주", "경기", "부산", "대전", "광주", "충북", "강원", "경남", "전남"}

for city in citys :
    for page in range(1, 115 + 1) :
        response = requests.post(
            "https://auction.realestate.daum.net/ajax/main_list.php",
            params = {
                "addr1": "서울",
                "result": 99,
                "yongdo": 99,
                "yongdo_detail": 99,
                "sort": "13D",
            },
            data = {
                "total": 1379,
                "block": page,
                "start": "",
                "next": "",
                "addr1": "서울",
                "addr2": "",
                "addr3": "",
                "bubcd": "",
                "kye": "",
                "local_num": "",
                "var_period": "",
                "result": 99,
                "var_kind": "",
                "yuchalcnt": "",
                "gamprice": "",
                "lowprice": "",
                "bdarea": "",
                "daejiarea": "",
                "ipchaltype": "", 
                "bdname": "",
                "special": "",
                "addshow": "",
                "sort": "13D",
                "subMenuIdx": 1,
            },
            headers = {
                "Referer": "https://auction.realestate.daum.net/v15/"
            }
        )

        #print(response.status_code)

        with open(f"./html/{city}/{page}page.html", 'w', encoding = "utf-8") as f:
            f.write(response.text)

        soup = BeautifulSoup(response.text, "html.parser")
        trs = soup.select(selector = '#frm_myreg > table > tbody > tr')

        if len(trs) == 0 :
            print(f"{page} 에서 ")
            break

        jsonpage = []
        for tr in trs:
            data = {
                "사건번호": (tr.select_one("td.no_bdL_check_new a").text),
                "물건용도": (tr.select_one("td.bottom9_new > div.ac_box > a > p.used").text),
                "소재지": (tr.select_one("td.bottom9_new > div.ac_box > a > p.address").text),
                "면적": (tr.select_one("td.bottom9_new > div.ac_box > p.area > span").text),
                "감정가": (tr.select_one("td.price_new > div.mapList_price.price_icon1 > p").text),
            }

            print('-' * 20)
            print(str(count) + "번째 " + data["사건번호"])
            
            datas.append(data)
            jsonpage.append(data)

            count += 1
        
        with open(f"./json/{city}/{page}page.json", 'w', encoding = "utf-8") as f:
            f.write(json.dumps(datas, ensure_ascii = False))
        
        time.sleep(5)

    with open("./ALL/{city}/all.json", 'w', encoding = "utf-8") as f:
        f.write(json.dumps(datas, ensure_ascii = False))