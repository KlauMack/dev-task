import os
from dotenv import load_dotenv

load_dotenv()

PORT = 8000

ENDPOINT = f"http://localhost:{PORT}"

EVENTS_FILE_PATH = f"src/event_propagator/events.json"

INTERVAL_SECONDS = 5

# REVIEW COMMENT:
# These env variables should be validated in some way. 
# Missing a variable in the env would result in auth or connection errors, that could be avoided with simple validation. 
# Would recommend using pydantic_settings.BaseSettings for this, as pydantic is already included in the project.
HEADERS = {
    "Authorization": "Bearer " + os.getenv("API_TOKEN"),
    "Content-Type": "application/json"
}

DB_URL=f"mysql+mysqldb://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOSTNAME')}:3306/{os.environ.get('DB_DATASET')}"
