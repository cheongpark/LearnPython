import json
from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

def _get_auctions() -> list:
    with open('./auctions.json', 'r', encoding = 'utf-8') as f:
        return json.loads(f.read())

def _save_auctions(auctions: list):
    with open('./auctions.json', 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(auctions, ensure_ascii = False))


if __name__ == '__main__': #이 파일만 테스트 할 때 다른 파일과 연결할 경우 이 것만 테스트 할 수 있도록
    print(type(_get_auctions()))
    print(_get_auctions().pop(1))

# 부동산 경매
# 1. 경매 목록 가져오기                   GET /auctions
# 2. 경매 목록 중 두번째 경매 가져오기     GET /auctions/2 
# 3. 경매 목록 중 두번째 경매 삭제하기     DELETE /auctions/2

@app.get('/')
def check():
    return {'status': 'check'}

@app.get('/auctions')
def get_auctions():
    return _get_auctions()

@app.get('/auctions/{id}')
def get_auction(id: int = Path(gt = 0)):
    # if id < 0: #-1 아래를 적을 경우 오류 (구식임)
    #     raise HTTPException(404) 

    try: #만약 리스트에 없을 경우 시도하고 안되면 except 실행
        return _get_auctions()[id - 1]
    except IndexError:
        raise HTTPException(404)

@app.delete('/auctions/{id}')
def del_auction(id: int = Path(gt = 0)):
    auctions = _get_auctions()
    try:
        auctions.pop(id - 1)
    except IndexError:
        raise HTTPException(404)
    _save_auctions(auctions)