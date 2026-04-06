from fastapi import FastAPI, HTTPException,Path, Query
import json

app = FastAPI()


def load_user_data():
    with open('info.json','r',newline='') as f:
        data = json.load(f)
        return data


@app.get('/users/{username}')
def get_users_by_name(username: str = Path(...,description='Username for fetching data')):
    data = load_user_data()
    flag = 0
    for user in data:
        flag = 1
        if username == user['username']:
            return user
           
    if not flag:
        raise HTTPException(status_code=404, detail=f'Invalid {username} is passed')

@app.get("/users")
def get_user_by_phone(phone: str = Query(...,description='User phone number')):
    data = load_user_data()
    for user in data:
        if phone == user['phoneNumber']:
            return user
    raise HTTPException(status_code=404,detail=f'Invalid {phone} phone is provided')


@app.get("/users/filter")
def filter(company: str = Query(), area: str = Query(None)):
    data = load_user_data()
    result  = []
    for user in data:
        descpt = user['job']
        if company is not None and descpt['company'] != company:
            continue
        if area is not None and descpt['area'] != area:
            continue 
        result.append(user)
    return result