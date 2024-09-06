from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Symbol(BaseModel):
    sym_id: int
    sym_path: str
    sym_group_id: int
    ten_id: int


symbols_list = [
    Symbol(sym_id=1, sym_path="/public/images/symbols/symbol1.png", sym_group_id=101, ten_id=1),
    Symbol(sym_id=2, sym_path="/public/images/symbols/symbol2.png", sym_group_id=102, ten_id=2),
    Symbol(sym_id=3, sym_path="/public/images/symbols/symbol3.png", sym_group_id=103, ten_id=1),
    Symbol(sym_id=4, sym_path="/public/images/symbols/symbol4.png", sym_group_id=104, ten_id=3),
    Symbol(sym_id=5, sym_path="/public/images/symbols/symbol5.png", sym_group_id=105, ten_id=2),
    Symbol(sym_id=6, sym_path="/public/images/symbols/symbol6.png", sym_group_id=106, ten_id=1),
    Symbol(sym_id=7, sym_path="/public/images/symbols/symbol7.png", sym_group_id=107, ten_id=3),
    Symbol(sym_id=8, sym_path="/public/images/symbols/symbol8.png", sym_group_id=108, ten_id=2),
    Symbol(sym_id=9, sym_path="/public/images/symbols/symbol9.png", sym_group_id=109, ten_id=1),
    Symbol(sym_id=10, sym_path="/public/images/symbols/symbol10.png", sym_group_id=110, ten_id=3)
]

@router.get("/symbols")
async def symbols():
    return symbols_list

@router.get("/symbol/{sym_id}")
async def symbol(sym_id: int):
    return search_symbol(sym_id)

@router.post("/symbol", response_model=Symbol, status_code=201)
async def symbol(symbol: Symbol):
    if type (search_symbol(symbol.sym_id)) == Symbol:
        raise HTTPException(status_code=384,detail="El símbolo ya existe")
    symbols_list.append(symbol)
    return symbol

def search_symbol(sym_id: int):
    symbols = filter(lambda symbol: symbol.sym_id == sym_id, symbols_list)
    
    try:
        return list(symbols)[0]
    except:
        return {"error":"No se ha encotrado el símbolo"}