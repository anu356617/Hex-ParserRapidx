# services/event_logger_service.py
from kink import inject
from repo.dbHandler import DBHandler

@inject
class EventLoggerService:
    def __init__(self, db_handler: DBHandler):
        self.db_handler = db_handler

    def process_event(self, event_message):
        # Assuming event_message is a dict
        self.db_handler.insert_events(event_message)
