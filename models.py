from pydantic import BaseModel, Field


class AEROPORTO(BaseModel):
    id: int
    codice: str = Field(min_length=3, max_length=3)
    citta: str

class AEROPORTO():
    id:int
    


