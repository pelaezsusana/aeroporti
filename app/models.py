from pydantic import BaseModel, Field, ConfigDict

class AEROPORTO_CREATE(BaseModel):
    codice: str = Field(..., min_length=3, max_length=3)
    citta: str

class AEROPORTO_RESPONSE():
    id:int
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    
