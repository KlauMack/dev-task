from fastapi import APIRouter, Depends, HTTPException

from src.event_consumer.authorization import verify_token
from src.event_consumer.database import DatabaseConnection
from src.event_consumer.model import Event

router = APIRouter(dependencies=[Depends(verify_token)])

@router.post("/event")
async def consume_event(event: Event):
    db_connection = DatabaseConnection()
    db_connection.add_event(event)

@router.get("/ready")
def ready():
    db_connection = DatabaseConnection()
    if db_connection.check_connection():
        return {"status": "ready"}
    else:
        raise HTTPException(status_code=500, detail="Database connection failed!")
