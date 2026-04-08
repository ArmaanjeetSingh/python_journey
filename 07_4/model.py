from pydantic import BaseModel, EmailStr, field_validator
from typing import List,Dict

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icic.com']
        #abc@gmail.compile
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()


    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,val):
        if 0 < val < 100:
            return val
        else:
            raise ValueError("Invalid age entered")

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.married)
    print(patient.weight)
    print("Patient updated in db")


patient_info = {'name':'armaan','email':'armaan@icic.com','age':'19','married':1,"weight":70.2,'allergies':['dust','pollen'],'contact_details':{'phone':'1234567890'}}
patient1 = Patient(**patient_info)#validation ---> type coercion
update_patient_data(patient1)
