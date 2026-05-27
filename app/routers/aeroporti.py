from fastapi import APIRouter, HTTPException
from app.models import AEROPORTO_CREATE
from app.database import aeroporti_db 
from app.logging_config import logger

router = APIRouter()


@router.get("/")
def get_aeroporti(page: int = 1, size: int = 5):
    logger.info(f"Fetching aeroporto page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    data = aeroporti_db[start:end]
    total_pages = (len(aeroporti_db) + size - 1)
    return {
        "page": page,
        "size": size,
        "total": total_pages,
        "data": data
    }


@router.get("/{aeroporto_id}")
def get_aeroporto(aeroporto_id: int):
    logger.info(f"Fetching book id={aeroporto_id}")
    for aeroporto in aeroporti_db:
        if aeroporto["id"] == aeroporto_id:
            return aeroporto
    raise HTTPException(status_code=404, detail="Aeroporto non trovato")


@router.post("/", status_code=201)
def create_aeroporto(aeroporto: AEROPORTO_CREATE):
    logger.info(f"Fetching create aeroporto with cita = {aeroporto.citta}")
    new_id = len(aeroporti_db) + 1
    new_aeroporto = {
        "id": new_id,
        "codice": aeroporto.codice,
        "citta": aeroporto.citta
    }

    aeroporti_db.append(new_aeroporto)
    return new_aeroporto


@router.delete("/{aeroporto_id}", status_code=204)
def delete_aeroporto(aeroporto_id: int):
    logger.info(f"Fetching delete aeroporto with id = {aeroporto_id}")
    for index, aeroporto in enumerate(aeroporti_db):
        if aeroporto["id"] == aeroporto_id:
            aeroporti_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="Aeroporto non trovato")