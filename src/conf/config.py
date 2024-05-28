import os
from dotenv import load_dotenv

load_dotenv()

PORT = 8000

ENDPOINT = f"localhost:{PORT}"

EVENTS_FILE_PATH = f"src/event_propagator/events.json"

INTERVAL_SECONDS = 5

HEADERS = {
    "Authorization": "Bearer " + os.getenv("API_TOKEN"),
    "Content-Type": "application/json"
}

DB_URL=f"mysql+mysqldb://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOSTNAME')}:3306/{os.environ.get('DB_DATASET')}"
