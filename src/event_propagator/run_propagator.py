import logging
from logging.config import fileConfig

from src.conf.config import ENDPOINT, EVENTS_FILE_PATH
from src.event_propagator.utils import read_events, send_events

fileConfig("src/conf/logger_conf.ini")

def run_propagator():
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info("Reading events from JSON file...")
    events = read_events(EVENTS_FILE_PATH)
    logging.info("Events read successfully.")

    logging.info("Sending events to the consumer...")
    send_events(ENDPOINT, events)
    logging.info("All events sent successfully.")

if __name__ == "__main__":
    run_propagator()