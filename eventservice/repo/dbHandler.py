from kink import di, inject
from utils.postgres_utils import get_session
from models.postgres.project import Eventlogs
from models.postgres.base import Base

@inject
class DBHandler():
    def insert_events(self, event_logs):
        with get_session() as session:
            new_event = Eventlogs(
                run_id=event_logs['runId'],
                parent_id=event_logs['parentId'],
                level=event_logs['level'],
                event_type=event_logs['EventType'],
                message=event_logs['Message'],
                start_date=event_logs.get('StartDate'),
                end_date=event_logs.get('EndDate')
            )
            session.add(new_event)
            session.commit()

    def create_table(self):
        with get_session() as session:
            Base.metadata.create_all(session.get_bind())
