# Event Propagator/Consumer Services

## Overview

- Event consumer service made to send JSON events periodically to HTTP API endpoint.
- RESTful API service created to catch incoming JSON events and upload them to the database.

## Features

- **Periodic JSON event send**: Sends JSON events every N seconds.
- **Database Operations**: Manage database resources with create, read, update and delete functionalities.
- **Data Validation**: Ensures data integrety and validation using **Pydantic** library.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Endpoints](#endpoints)
4. [Authentication](#authentication)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/KlauMack/dev-task.git
cd dev-task
```
2. **Install dependencies:**
```bash
make install
```
3. **Configure environment variables:**
Create a `.env` according to `.env.example` file in the root directory and add the following variables:
```bash
# Database configurations
DB_HOSTNAME="{value}"
DB_USER="{value}"
DB_PASSWORD="{value}"
DB_DATASET="{value}"

# JWT token configurations
API_TOKEN="{value}"
SECRET_KEY="{value}"
ALGORITHM="{value}"
```
4. **Run event consumer:**
```bash
make run_consumer
```

**Run event propagator:**
```bash
make run_propagator
```

## Usage

After starting the event consumer service, the API will be available at `http://locahost:8000`

## Endpoints

- **Check database/service ready status**
```bash
GET /api/ready
```
**Response**
```bash
[
    {
        {"status": "ready"}
    }
]
```

- **Consume incoming events and populate the database**
```bash
POST /api/event
```
**Request body**
```bash
[
    {
        "event_type": "string",
        "event_payload": "string"
    }
]
```
**Response**
```bash
[
    {
        {"status_code": "200"}
    }
]
```

## Endpoints

All calls to the API service requires an API token (generated using **pyjwt** library) with FastAPI's **OAuth2PasswordBearer** library. Header example:
```bash
{
    "Authorization": "Bearer " + {"API_TOKEN"},
    "Content-Type": "application/json"
}
```
