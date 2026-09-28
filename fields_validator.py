from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, field_validator


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: Optional[bool] = False
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}
    linkedin_url: Optional[HttpUrl] = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domains = ["hdfc.com", "icicibank.com"]
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Domain must be one of: {', '.join(valid_domains)}")
        return value
    @field_validator("name" , mode='before')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError("Name must be less than 50 characters")
        return value
    def upp_name(cls , value : str) -> str:
        return value.upper()
    
    @field_validator('age' , mode = 'after') 
    @classmethod
    def validate_age(cls , value : int) -> int: 
        if value < 0 or value > 120:
            raise ValueError('Age must be between 0 and 120')
        return value
def print_info_patient(patient: Patient) -> None:
    
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Allergies:", patient.allergies)
    print("Married:", patient.married)
    print("Email:", patient.email)
    print("LinkedIn:", patient.linkedin_url)
    print("Weight:", patient.weight)
    print("Height:", patient.height)
    print("Status: uploaded")


# Sample data
patient_info = {
    "name": "nitish",
    "email": "abc@hdfc.com",  # Must use a valid domain from valid_domains
    "linkedin_url": "http://linkedin.com/1322",
    "age": "30",  # Automatically converted to int
    "weight": "75.2",  # Automatically converted to float
    "height": 175.0,
    "contact_details": {"phone": "2353462"},
}

# Instantiate model and call print function
patient_1 = Patient(**patient_info)
print_info_patient(patient_1)