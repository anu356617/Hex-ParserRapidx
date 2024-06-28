# app.py
from dotenv import load_dotenv
import logging.config
import os
import sys
from kink import di
from utils.queue_utils import bind_consumer, channel, connection
from services.queue_service import EventLoggerService
from utils.utils import get_logging_config
from utils.di_setup import setup_di
import json

# Load environment variables
load_dotenv()

# Setup logging
config_file_path = get_logging_config()
logging.config.fileConfig(config_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@bind_consumer(queue=os.environ.get('EVENT_LOG_QUEUE_NAME'))
def consume_event_log_queue(ch, method, properties, body):
    try:
        event_logger_service = di[EventLoggerService]
        event_message = json.loads(body)
        event_logger_service.process_event(event_message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():
    # Setup DI container
    setup_di()

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        connection.close()

if __name__ == "__main__":
    main()
