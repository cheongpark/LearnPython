from fastapi import FastAPI

app = FastAPI()

@app.get('/hello') #: 행위 / 자원
def hello():
    return {'test': 'hello2'} #: 표현


#post나 get으로 하면 같은 URL이라도 다르게 사용 가능
@app.post('/users') #: 행위 / 자원
def create_user(username: str):
    return {'username': username}

@app.get('/users') #: 행위 / 자원
def get_users(username: str):
    return {'username': username}

#파라미터 없이 패스로 넘기기 (패스 파라미터)
@app.get('/users/{username}') #: 행위 / 자원
def get_user(username: str):
    return {'username': username}

