import os
from utils.postgres_utils import get_session
from repo.dbHandler import DBHandler
from services.queue_service import EventLoggerService

def setup_di():
    # postgres_url = os.environ.get('POSTGRES_URL')
    queue_name = os.environ.get('EVENT_LOG_QUEUE_NAME')
    rabbitmq_url = os.environ.get('RABBITMQ_URL')
    
    di = {}
    di[DBHandler] = DBHandler()
    db_handler = di[DBHandler]
    db_handler.create_table()

    di[EventLoggerService] = EventLoggerService(db_handler)

    return di
