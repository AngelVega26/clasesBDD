from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
<<<<<<< HEAD
    name:str
    email: str
    password: str
    
=======
    name: str
    email: str
    password: str
>>>>>>> origin/ThunderGer
