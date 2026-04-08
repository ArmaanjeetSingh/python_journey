from fastapi import FastAPI, Path, HTTPException, Query

app = FastAPI()

users = [
    {"id": 1, "name": "Aman", "age": 21, "city": "Delhi"},
    {"id": 2, "name": "Rohit", "age": 25, "city": "Mumbai"},
    {"id": 3, "name": "Neha", "age": 22, "city": "Delhi"},
]

@app.get("/")
def welcome():
    return "Welcome  to Task API"

# /users/filter?city=Delhi&sort_by=age&order=desc&page=1&limit=2
@app.get("/users/sort")
def sort_users(sort_by: str = Query(...), order: str = Query(...)):
    
    if sort_by != 'age':
        raise HTTPException(status_code=400, detail='Invalid field')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order')

    reverse_order = True if order == 'desc' else False

    sorted_data = sorted(
        users,
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )

    return sorted_data


@app.get("/users/{id}")
def get_user_by_id(id: int = Path(...)):
    result = []
    for user in users:
        if user['id'] == id:
            result.append(user)
    if not result:
       raise HTTPException(status_code=404,detail="ID not found")
    else:
        return result

# /users/filter?city=Delhi&min_age=21
@app.get("/user/filter")
def filter_users(city: str = Query(None), min_age: int = Query(None)):
    result = []
    for user in users:
        if city is not None and city != user.get('city'):
            continue
        if min_age is not None and min_age > user.get('age'):
            continue
        result.append(user)
    return result

