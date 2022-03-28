import email
from typing import Optional
from click import password_option
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str