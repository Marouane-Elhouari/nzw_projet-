
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length =50 , title = 'Name of the patient' , description = 'give me your name less of 50 characters ' )]
    email:Annotated[EmailStr , Field(regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' , description = 'email of the patient') ]

    age: Annotated[int , Field(gt = 0 ,lt = 120)]
    linkedin_url: HttpUrl
    #FIeLD FOR COndition validations and annonated for mix the conditions type and extraconditions 
    weight: Annotated[float , Field(gt = 0 ,strict = True)]
    height: float = Field(..., gt=0)
    married: Annotated[bool, Field(default=False)] 
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str, str]



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.height)
    print('uploaded')


patient_info = {
    'name': 'nitish',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': '30',
    'weight': '75.2',
    'height': 175.0,
    'contact_details': {'phone': '2353462'},
}

patient_1 = Patient(**patient_info)
insert_patient_data(patient_1)