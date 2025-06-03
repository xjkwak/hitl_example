from pydantic import BaseModel, Field

class CrewInput(BaseModel):
    initial_message: str = Field(..., description="Initial message from the person")

class PersonalInformationOutput(BaseModel):
    first_name: str = Field(default="UNKNOWN", description="Person's first name")
    last_name: str = Field(default="UNKNOWN", description="Person's last name")
    country: str = Field(default="UNKNOWN", description="Person's country of residence")
    city: str = Field(default="UNKNOWN", description="Person's city of residence")
    company: str = Field(default="UNKNOWN", description="Person's company name")
    email: str = Field(default="UNKNOWN", description="Person's email")