import logging
from .database import aeroporti_db 

logger = logging.getLogger(__name__)


def get_aeroporti(page: int = 1, size: int = 5):
    logger.info(f"Fetching aeroporto page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    return aeroporti_db[start:end]


def get_book(aeroporto_id: int):
    logger.info(f"Fetching book id={aeroporto_id}")
    for aeroporto in aeroporti_db:
        if aeroporto["id"] == aeroporto_id:
            return aeroporto
    logger.warning(f"aeroporto id={aeroporto_id} not found")
    return None


def create_aeroporto(aeroporto_data: dict):
    new_id = len(aeroporti_db) + 1
    new_aeroporto = {"id": new_id, **aeroporto_data}
  
    aeroporti_db.append(new_aeroporto)
    logger.info(f"Book created id={new_id}")
    return new_aeroporto
