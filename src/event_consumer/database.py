from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.conf.config import DB_URL

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    event_type = Column(String(255))
    event_payload = Column(String(255))


class DatabaseConnection():
    def __init__(self):
        self._engine = create_engine(DB_URL)
        self._Session = sessionmaker(bind=self._engine)
        Base.metadata.create_all(self._engine)

    def check_connection(self) -> bool:
        try:
            conn = self._engine.connect()
            conn.close()
            return True
        except:
            return False
    
    def add_event(self, event: Event) -> None:
        session = self._Session()
        try:
            event_entry = Event(event_type=event.event_type, event_payload=event.event_payload)
            session.add(event_entry)
            session.commit()
            session.close()
        except Exception as e:
            session.rollback()
            session.close()
            raise e
    
    def read_records(self) -> Event:
        session = self._Session()
        try:
            events = session.query(Event).all()
            for event in events:
                print((event.id, event.event_type, event.event_payload))
            session.close()
        except Exception as e:
            session.rollback()
            session.close()
            raise e
    
    def update_event(self, event_id: int, event_type: str) -> None:
        session = self._Session()
        try:
            event = session.query(Event).filter_by(id=event_id).first()
            if event:
                event.event_type = event_type
                session.commit()
                session.close()
        except Exception as e:
            session.rollback()
            session.close()
            raise e
    
    def delete_event(self, event_id: int) -> None:
        session = self._Session()
        try:
            event = session.query(Event).filter_by(id=event_id).first()
            if event:
                session.delete(event)
                session.commit()
                session.close()
        except Exception as e:
            session.rollback()
            session.close()
            raise e
