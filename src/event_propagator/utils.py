import json
import logging
import random
import time
from logging.config import fileConfig
from typing import List

import requests

from src.conf.config import HEADERS, INTERVAL_SECONDS

fileConfig("src/conf/logger_conf.ini")


def read_events(file_path: str) -> List[dict]:
    """
    Read events from JSON file and returns the parsed data.

    Args:
        file_path (str): Path to the JSON file
    
    Returns:
        A list of events from the JSON file

    Raises:
        FileNotFoundError: if file is not found
        Exception: if unexpected error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            events_data = json.load(file)
        return events_data
    # REVIEW COMMENT:
    # An exception here would cause unexpected behaviour when using the function, since it would just return `None` after logging.
    # In our case it would result in a `TypeError`, since we would pass `None` to `random.choice()` in the `send_events` function.
    # The correct behaviour here would be to either reraise the exception of raise a custom one, indicating what went wrong.
    except FileNotFoundError:
        logging.error(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def send_events(base_url: str, events: List[dict]) -> None:
    """
    Send JSON data to an endpoint.

    Args:
        base_url (str): The base URL of the endpoint to send data to.
        events (List[dict]): The JSON data to send.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the event send operation.
    """
    # REVIEW COMMENT:
    # This logic has 4 nesting levels, which makes the function hard to read and test.
    # One nesting level could be avoided by checking `if not check_status` and returning afterwards, instead of dumping everything under the `if` statement. Such as:
    #
    # if not check_status(base_url):
    #   logging.warning("API is not ready yet, try again in a few seconds.")
    #   return
    # while events: ...

    if check_status(base_url):
        while events:
            random_event = random.choice(events)
            try:
                # REVIEW COMMENT:
                # Nitpick, but it would be safer to use something like urllib.parse.urljoin to construct the URL here.
                # It would break if the `base_url` was defined with a `/` at the end. 
                response = requests.post(base_url + "/event", headers=HEADERS, json=random_event)

                if response.status_code == 200:
                    logging.info(f"Event sent successfully.")
                else:
                    logging.warning(f"Failed to send an event. Status code: {response.status_code}, Detail: {response.text}")
                
                time.sleep(INTERVAL_SECONDS)

            except Exception as e:
                logging.error("An error occurred:", str(e))
                time.sleep(INTERVAL_SECONDS)
    else:
        logging.warning("API is not ready yet, try again in a few seconds.")


def check_status(endpoint_url: str) -> bool:
    """Checks endpoint ready status."""
    response = requests.get(endpoint_url + "/ready", headers=HEADERS)
    # REVIEW COMMENT:
    # Nitpick, but could be rewritten as a oneliner.
    # `return response.status_code == 200 and response.json()["status"] == "ready"`

    # Check if the response indicates readiness
    if response.status_code == 200 and response.json()["status"] == "ready":
        return True
    else:
        return False
