from datetime import date
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Process(BaseModel):
    pro_id: int
    pro_pages: int
    pro_name: str
    pro_group_id: int
    pro_type_id: int
    ten_id: int
    cust_id: int
    pro_status: str
    pro_upload_date: str
    pro_update_date: str
    pro_tipo: str
    pro_precision: int
    pro_archivos: int

process_list = [
    Process(pro_id=1, pro_pages=5, pro_name="Proceso 1", pro_group_id=1, pro_type_id=1, ten_id=1, cust_id=101, pro_status="finalizado", pro_upload_date="2024-08-10", pro_update_date="2024-08-20", pro_tipo="Técnico",pro_precision=97, pro_archivos=4),
    Process(pro_id=2, pro_pages=12, pro_name="Proceso 2", pro_group_id=2, pro_type_id=2, ten_id=2, cust_id=102, pro_status="progreso", pro_upload_date="2024-07-10", pro_update_date="2024-08-20",pro_tipo="Técnico",pro_precision=100, pro_archivos=8),
    Process(pro_id=3, pro_pages=7, pro_name="Proceso 3", pro_group_id=3, pro_type_id=1, ten_id=1, cust_id=103, pro_status="finalizado", pro_upload_date="2024-06-10", pro_update_date="2024-07-20",pro_tipo="Técnico",pro_precision=92, pro_archivos=10),
    Process(pro_id=4, pro_pages=20, pro_name="Proceso 4", pro_group_id=4, pro_type_id=3, ten_id=2, cust_id=104, pro_status="progreso", pro_upload_date="2024-05-10", pro_update_date="2024-06-20",pro_tipo="Técnico",pro_precision=80, pro_archivos=23),
    Process(pro_id=5, pro_pages=25, pro_name="Proceso 5", pro_group_id=5, pro_type_id=4, ten_id=3, cust_id=105, pro_status="finalizado", pro_upload_date="2024-04-10", pro_update_date="2024-05-20",pro_tipo="Técnico",pro_precision=99, pro_archivos=1),
    Process(pro_id=6, pro_pages=8, pro_name="Proceso 6", pro_group_id=6, pro_type_id=2, ten_id=1, cust_id=106, pro_status="progreso", pro_upload_date="2024-03-10", pro_update_date="2024-04-20",pro_tipo="Técnico",pro_precision=100, pro_archivos=4),
    Process(pro_id=7, pro_pages=30, pro_name="Proceso 7", pro_group_id=7, pro_type_id=1, ten_id=3, cust_id=107, pro_status="finalizado", pro_upload_date="2024-02-10", pro_update_date="2024-03-20",pro_tipo="Técnico",pro_precision=97, pro_archivos=3),
    Process(pro_id=8, pro_pages=15, pro_name="Proceso 8", pro_group_id=8, pro_type_id=3, ten_id=2, cust_id=108, pro_status="progreso", pro_upload_date="2024-01-10", pro_update_date="2024-02-20",pro_tipo="Técnico",pro_precision=100, pro_archivos=9),
    Process(pro_id=9, pro_pages=10, pro_name="Proceso 9", pro_group_id=9, pro_type_id=4, ten_id=1, cust_id=109, pro_status="finalizado", pro_upload_date="2023-12-10", pro_update_date="2024-01-20",pro_tipo="Técnico",pro_precision=91, pro_archivos=12),
    Process(pro_id=10, pro_pages=18, pro_name="Proceso 10", pro_group_id=10, pro_type_id=2, ten_id=3, cust_id=110, pro_status="progreso", pro_upload_date="2023-08-10", pro_update_date="2023-12-20",pro_tipo="Técnico",pro_precision=90, pro_archivos=52)
]


@router.get("/processes")
async def process():
    return process_list

@router.get("/process/{doc_id}")
async def process(doc_id: int):
    return search_process(doc_id)

@router.post("/process/", response_model=Process)
async def process(process: Process):
    if type(search_process(process.pro_id)) == Process:
        raise HTTPException(detail="El proceso ya existe")
    
    process_list.append(process)
    return process

@router.get("/ruta")
async def greet(name: str, id_cliente: int, id_usuario: int):
    return {"ruta": f"{name}"}


def search_process(pro_id: int):
    process = filter(lambda process: process.pro_id == pro_id, process_list)
    try:
        return list(process)[0]
    except:
        return {"error":"No se ha encotrado el proceso"}
    
