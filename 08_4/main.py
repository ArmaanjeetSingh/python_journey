from fastapi import FastAPI,Path, HTTPException, Query
from pydantc import BaseModel
import json

app = FastAPI()

class Patient(BaseModel):
    id : str
    name : str
    city : str
    age : int
    gender : str
    height : float
    weight : float



def load_patient_data():
    with open("patient.json","r") as file:
        data = json.load(file)
        return data

@app.get("/")
def hello():
    return {'message':'hello world'}

@app.get("/about")
def about():
    return {'message':'FastApi is modern high performance framework for building APIs using python'}

@app.get("/patient")
def view():
    data = load_patient_data()
    return data

@app.get('/patient/{patient_id}')
def get_by_patient_id(patient_id: str = Path(...,description='ID of the patient in the db',examples='P001')):
    #load all patients
    data = load_patient_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basis of height, weight or bmi'), order: str = Query('asc',description='Sort in ascending or descending order')):

    valid_fields = ["height","weight","bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'invalid field select from {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f'Invalid order select between asc and desc')

    data = load_patient_data()
    sort_order = True if order=='asc' else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.get("/filter")
def filter_patients(min_range : int = Query(None),
                    max_range: int = Query(None),
                    city : str = Query(None)):
    result = []
    data = load_patient_data()
    if min_range is not None and max_range is not None and min_range > max_range:
        raise HTTPException(status_code=400,detail = "invalid range")
    for patient_id in data:
        patient1 = data[patient_id]
        age = patient1['age']
        patient_city = patient1.get('city')
        if min_range is not None and min_range > age:
            continue
        if max_range is not None and max_range < age:
            continue
        if city is not None and city != patient_city:
            continue
        else:
            result.append(data[patient_id])
    return result
