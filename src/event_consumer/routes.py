from fastapi import APIRouter, Depends, HTTPException

from src.event_consumer.authorization import verify_token
from src.event_consumer.database import DatabaseConnection
from src.event_consumer.model import Event

router = APIRouter(dependencies=[Depends(verify_token)])

@router.post("/event")
async def consume_event(event: Event):
    db_connection = DatabaseConnection()
    # REVIEW COMMENT:
    # This is a synchronous method used in an async context. This would block the entire main thread until it finishes running.
    # Synchronous I/O methods shouldn't be used in an async context at all.
    db_connection.add_event(event)

@router.get("/ready")
def ready():
    db_connection = DatabaseConnection()
    if db_connection.check_connection():
        return {"status": "ready"}
    # REVIEW COMMENT:
    # Unnecessary `else` statement. The above clause returns, so there's no need to have `else` here.
    else:
        # REVIEW COMMENT:
        # Bit of a nitpick, but FastAPI returns 500 by default, if an error is raised. Therefore, a more informative exception could be raised here.
        # Also, a 500 error code shouldn't send any details about the error to the client, so this detail is unnecessary.
        raise HTTPException(status_code=500, detail="Database connection failed!")
