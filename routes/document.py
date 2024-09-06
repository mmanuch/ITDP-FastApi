from datetime import date
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Document(BaseModel):
    doc_nombre:str
    doc_tipo:str
    doc_proceso:str
    doc_precision:int
    doc_pages:int
    doc_fecha: str
    doc_status: str

document_list = [
    Document(doc_nombre="Laser Lemonade Machine", doc_tipo="Técnico", doc_proceso="Categoría 1", doc_precision=97, doc_pages=25, doc_fecha="2024-07-12 10:42 AM", doc_status="finalizado"),
    Document(doc_nombre="Hypernova Headphones", doc_tipo="Factura", doc_proceso="Categoría 2", doc_precision=98, doc_pages=2, doc_fecha="2024-8-18 03:21 PM", doc_status="finalizado"),
    Document(doc_nombre="AeroGlow Desk Lamp", doc_tipo="Técnico", doc_proceso="Categoría 3", doc_precision=94, doc_pages=30, doc_fecha="2023-11-29 08:15 AM", doc_status="finalizado"),
    Document(doc_nombre="TechTonic Energy Drink", doc_tipo="Pedido", doc_proceso="Categoría 1", doc_precision=100, doc_pages=7, doc_fecha="2023-12-25 11:59 PM", doc_status="progreso"),
    Document(doc_nombre="Gamer Gear Pro Controller", doc_tipo="Ticket", doc_proceso="Categoría 4", doc_precision=99, doc_pages=5, doc_fecha="2024-01-01 12:00 AM", doc_status="finalizado"),
    Document(doc_nombre="Luminous VR Headset", doc_tipo="Ticket", doc_proceso="Categoría 6", doc_precision=97, doc_pages=3, doc_fecha="2024-02-14 02:14 PM", doc_status="progreso"),
    Document(doc_nombre="Quantum Keyboard", doc_tipo="Ticket", doc_proceso="Categoría 2", doc_precision=100, doc_pages=11, doc_fecha="2023-06-30 09:45 AM", doc_status="finalizado"),
    Document(doc_nombre="Echo Wireless Mouse", doc_tipo="Técnico", doc_proceso="Categoría 1", doc_precision=100, doc_pages=20, doc_fecha="2023-08-10 10:30 AM", doc_status="progreso"),
    Document(doc_nombre="Neon Flex Monitor Stand", doc_tipo="Pedido", doc_proceso="Categoría 1", doc_precision=100, doc_pages=4, doc_fecha="2023-09-01 02:30 PM", doc_status="progreso"),
    Document(doc_nombre="Aurora RGB Speakers", doc_tipo="Factura", doc_proceso="Categoría 10", doc_precision=100, doc_pages=10, doc_fecha="2023-11-20 01:15 PM", doc_status="finalizado")
]


@router.get("/documentos")
async def documents():
    return document_list

@router.get("/documentos/paginas")
async def paginas():
    total_paginas = contar_paginas(document_list)
    return total_paginas

@router.get("/documentos/finalizados")
async def finalizados():
    total_finalizados = contar_finalizados(document_list)
    return total_finalizados

@router.get("/document/{doc_id}")
async def document(doc_id: int):
    doc = search_document(doc_id)
    if not isinstance(doc, Document):
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return doc

@router.post("/document/", response_model=Document)
async def add_document(document: Document):
    if isinstance(search_document(document.doc_id), Document):
        raise HTTPException(status_code=400, detail="El documento ya existe")
    
    document_list.append(document)
    return document

def search_document(doc_id: int):
    documents = list(filter(lambda document: document.doc_id == doc_id, document_list))
    
    if documents:
        return documents[0]
    return None

def contar_paginas(document_list):
    total_paginas = sum(document.doc_pages for document in document_list)
    return total_paginas

def contar_finalizados(document_list):
    total_finalizados = sum(1 for document in document_list if document.doc_status == "finalizado")
    return total_finalizados