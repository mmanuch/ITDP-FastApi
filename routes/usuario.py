
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Usuario(BaseModel):
    email: str
    password: str

user_list = [
    Usuario(email="manu@ejemplo.com", password="1234"),
    Usuario(email="paco@ejemplo.com", password="12345"),
]

@router.post("/usuarios")
async def categories():
    return user_list
