import logging
from logging.config import fileConfig

import uvicorn
from fastapi import FastAPI

from src.conf.config import PORT
from src.event_consumer.routes import router

fileConfig("src/conf/logger_conf.ini")

app = FastAPI()

app.include_router(router)

def run_consumer():
    logging.info("Running event consumer...")
    uvicorn.run("src.event_consumer.run_consumer:app", reload=True, port=PORT)

if __name__ == "__main__":
    run_consumer()
