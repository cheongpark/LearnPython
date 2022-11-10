import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def _get_auctions() -> list:
    with open('auctions.json', 'r', encoding = 'utf-8') as f:
        return json.loads(f.read())

def _save_auctions(auctions: list):
    with open('auctions.json', 'w', encoding = 'utf-8') as f:
        f.write(json.dump(auctions, ensure_ascii = False))

if __name__ == '__main__':
    print(_get_auctions())

@app.get('/apis/auctions')
def get_auctions():
    return _get_auctions()

@app.get('/auctions')
def get_auctions_html():
    with open('auctions.html', 'r', encoding = 'utf-8') as f:
        return HTMLResponse(f.read())