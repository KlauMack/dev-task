import unittest

from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from src.event_consumer.database import DatabaseConnection

Base = declarative_base()

class TestEvent(Base):
    __tablename__ = "test_events"

    id = Column(Integer, primary_key=True)
    event_type = Column(String(255))
    event_payload = Column(String(255))

db_connection = DatabaseConnection()

class TestDatabase(unittest.TestCase):
    def test_add_event(self):
        Base.metadata.create_all(db_connection._engine)
        new_event = TestEvent(event_type="test_type", event_payload="test_payload")
        session = db_connection._Session()
        session.add(new_event)
        session.commit()
        self.assertIsNotNone(new_event.id)

    