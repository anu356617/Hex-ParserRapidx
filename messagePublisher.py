import pika
import json

# RabbitMQ connection parameters
credentials = pika.PlainCredentials('lxptmxtz', 'xuBCHtJkSOBnUUHYcI8hht9A3uw1G_Dy')
parameters = pika.ConnectionParameters(
    host='puffin-01.rmq2.cloudamqp.com',
    port=5672,
    virtual_host='lxptmxtz',
    credentials=credentials,
    ssl_options=None
)

# Establish connection
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare queue
queue_name = 'dev_queue'
channel.queue_declare(queue=queue_name, durable=True)

def generateNumberofmessages(records):
    data = []
    for i in range(records):
        record =  {"runId": 1, "parentId": 1, "level": f"Testing {i + 20}", "EventType": "Check", "Message": "Check Completed"}
        data.append(record)
    return data


records = 200
sample_messages =  generateNumberofmessages(records)

# Sample messages
# sample_messages = [
#     {"runId": 1, "parentId": 1, "level": "Test", "EventType": "Check", "Message": "Check Completed"}
# ]

# Publish messages to the queue
for message in sample_messages:
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    print(f"Sent message: {message}")

# Close connection
connection.close()