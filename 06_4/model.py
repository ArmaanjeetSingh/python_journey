from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List,Dict, Optional, Annotated

class Patient(BaseModel):
    # name : str = Field(max_length=20)
    name:Annotated[str,Field(max_length=50, title="name of the patient", description='Give the name of patient with length not more than 5',examples=['Armaan','Harry'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age : int = Field(gt=0,lt=90)
    weight : float = Field(gt = 0)
    married:Optional[bool] = 0
    # allergies: Optional[List[str]] = Field(max_length=5)
    allergies: Annotated[Optional[List[str]], Field(max_length=5,default=None)]
    contact_details: Dict[str,str]


def insert_patient_data(patient : Patient):
    print(patient.name, patient.age, patient.weight)
    print(patient.allergies)
    print(patient.married)
    print("Inserted into database")

def update_patient_data(patient: Patient):
    print(patient.name,patient.age)


patient_info = {"name":'armaan',"age":28,"weight":52.5,"allergies":['pollen','dust'],'contact_details':{'phone':'1234567'},'email':'abc@gmail.com','linkedin_url':'https://linkedin.com/?name=armaan'}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)