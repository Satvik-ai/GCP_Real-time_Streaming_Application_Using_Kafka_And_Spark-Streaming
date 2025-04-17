"""Task: Write a Producer that reads from that file, breaks the data into batches of 10 records, and writes to Kafka, 
such that each batch is separated by a sleep time of 10 seconds from the previous batch. 
The Producer can stop emitting once 1000 records are written."""

import time
from google.cloud import storage
from kafka import KafkaProducer

BUCKET_NAME = "satvik-storage-bucket"
FILE_NAME = "input_data.csv"
KAFKA_TOPIC = "input-topic"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, value_serializer=lambda x: x.encode('utf-8'))

# Download file from GCS
client = storage.Client()
bucket = client.bucket(BUCKET_NAME)
blob = bucket.blob(FILE_NAME)
data = blob.download_as_text().split("\n")

batch_size = 10
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    if not batch or batch[0] == "":
        continue
    
    for record in batch:
        producer.send(KAFKA_TOPIC, record)
    
    print(f"Sent batch {i//batch_size + 1}")
    time.sleep(10)  # 10 seconds delay

print("Producer finished sending messages.")
producer.close()