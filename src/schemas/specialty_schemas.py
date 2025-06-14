from pydantic import BaseModel

class SpecialtyBase(BaseModel):
    name: str
    description: str

class SpecialtyCreate(SpecialtyBase):
    pass

class SpecialtyOut(SpecialtyBase):
    id: int

    class Config:
        from_attributes = True