from pydantic import BaseModel, EmailStr, model_validator, computed_field
from typing import List,Dict

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    height : float
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in  model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact')

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.married)
    print(patient.weight)
    print("Patient updated in db")
    print(patient.calculate_bmi)


patient_info = {'name':'armaan','email':'armaan@icic.com','age':'79',"height":1.63,'married':1,"weight":70.2,'allergies':['dust','pollen'],'contact_details':{'emergency':'1234567890'}}
patient1 = Patient(**patient_info)#validation ---> type coercion
update_patient_data(patient1)
