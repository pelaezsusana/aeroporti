from fastapi import APIRouter, HTTPException
from typing import List
from ..models import aeroporti
from .. import crud





@router.get("", response_model=List[aeroporti])
def list_AEROPORTO(page: int = 1, size: int = 10):
    return crud.get_aeroporto(page, size)


@router.get("/{aeroporto_id}", response_model=aeroporti)
def get_AEROPORTO(aeroporto_id: int):
    aeroporti = crud.get_aeroporto(aeroporto_id)
    if not aeroporti:
        raise HTTPException(status_code=404, detail="AEROPORTO not found")
    return aeroporti


@router.post("", response_model=aeroporti, status_code=201)
def create_aeroporto(aeroporto: aeroporti):
    return crud.create_book(aeroporti.dict())