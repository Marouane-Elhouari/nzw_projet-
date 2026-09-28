from pydantic import BaseModel, EmailStr, model_validator , computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    @computed_field()
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '10', 'weight': 75.2,"height": 175.0, "linkedin_url": "http://linkedin.com/1322", 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)