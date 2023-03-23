import datetime as _dt
# pydantic is a library for data validation and serialization. 
# It is used to create models that can be used to validate and serialize data.
import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email: str
    

class UserCreate(_UserBase):
    hashed_password: str
    
    class Config:
        orm_mode = True
        
        
class User(_UserBase):
    id: int
    
    class Config:
        orm_mode = True
        

class _LeadBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str = ""
    note: str = ""
    

class LeadCreate(_LeadBase):
    owner_id: int
    
    class Config:
        orm_mode = True
        
        
class Lead(_LeadBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_updated: _dt.datetime
    
    class Config:
        orm_mode = True
        
# Path: backend/main.py