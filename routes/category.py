from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Category(BaseModel):
    cat_id: int
    cat_name: str
    cat_description: str
    cat_status: str

class CategorySymbol(BaseModel):
    cat_name: str
    cat_status: str

category_list = [
    Category(cat_id=101, cat_name="Category 1", cat_description="Description for Category 1", cat_status="hecho"),
    Category(cat_id=102, cat_name="Category 2", cat_description="Description for Category 2", cat_status="nuevo"),
    Category(cat_id=103, cat_name="Category 3", cat_description="Description for Category 3", cat_status="nuevo"),
    Category(cat_id=104, cat_name="Category 4", cat_description="Description for Category 4", cat_status="nuevo"),
    Category(cat_id=105, cat_name="Category 5", cat_description="Description for Category 5", cat_status="hecho"),
    Category(cat_id=106, cat_name="Category 6", cat_description="Description for Category 6", cat_status="hecho"),
    Category(cat_id=107, cat_name="Category 7", cat_description="Description for Category 7", cat_status="hecho"),
    Category(cat_id=108, cat_name="Category 8", cat_description="Description for Category 8", cat_status="nuevo"),
    Category(cat_id=109, cat_name="Category 9", cat_description="Description for Category 9", cat_status="hecho"),
    Category(cat_id=110, cat_name="Category 10", cat_description="Description for Category 10", cat_status="nuevo")
]

category_list_symbol = [
    CategorySymbol(cat_name="Uno", cat_status="hecho"),
    CategorySymbol(cat_name="Dos", cat_status="hecho"),
    CategorySymbol(cat_name="Tres", cat_status="nuevo"),
    CategorySymbol(cat_name="Cuatro", cat_status="nuevo"),
    CategorySymbol(cat_name="Cinco", cat_status="nuevo"),
    CategorySymbol(cat_name="Seis", cat_status="hecho"),
]

@router.get("/categories/symbols")
async def categories():
    return category_list_symbol

@router.get("/categories")
async def categories():
    return category_list

@router.get("/category/name")
async def category():
    nombres_categorias = obtener_nombres_categorias(category_list)
    return nombres_categorias

@router.get("/category/{cat_id}")
async def category(cat_id: int):
    return search_category(cat_id)

@router.post("/category", response_model=Category, status_code=201)
async def category(symbol: Category):
    if type (search_category(symbol.sym_id)) == Category:
        raise HTTPException(status_code=384,detail="La categoría ya existe")
    category_list.append(symbol)
    return symbol

@router.delete("/category/{cat_id}", status_code=204)
async def delete_category(cat_id: int):
    global category_list
    category_list = [cat for cat in category_list if cat.cat_id != cat_id]
    return


def search_category(cat_id: int):
    categories = filter(lambda category: category.cat_id == cat_id, category_list)
    
    try:
        return list(categories)[0]
    except:
        return {"error":"No se ha encotrado la categoría"}
    
def obtener_nombres_categorias(category_list):
    nombres = [category.cat_name for category in category_list]
    return nombres
