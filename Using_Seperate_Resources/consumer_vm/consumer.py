"""Task: Write a Spark Streaming consumer that reads from the same Kafka topic every 5 seconds 
and emits count of rows seen in the last 10 seconds."""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window

KAFKA_TOPIC = "input-topic"
KAFKA_BOOTSTRAP_SERVERS = "34.31.111.198:9092"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaSparkStreamingConsumer") \
    .getOrCreate()

# Print debug information
print(f"Connecting to Kafka broker at {KAFKA_BOOTSTRAP_SERVERS}")
print(f"Subscribing to topic {KAFKA_TOPIC}")

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "earliest") \
    .load()

# Deserialize JSON messages and keep the timestamp field
df = df.selectExpr("CAST(value AS STRING) AS value", "timestamp")

# Count records using a sliding window of 10 seconds that slides every 5 seconds
df_count = df.groupBy(window(col("timestamp"), "10 seconds", "5 seconds")).count()

"""Sliding Window: window(col("timestamp"), "10 seconds", "5 seconds") creates windows that are 10 seconds long and start every 5 seconds. 
This means each output will count records received in the last 10 seconds."""

# Sort the output by the start of the window
df_count_sorted = df_count.orderBy(col("window.start"))

# Output count to console with processing trigger every 5 seconds
query = df_count_sorted.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("numRows", "1000") \
    .option("truncate", "false") \
    .trigger(processingTime="5 seconds") \
    .start()

"""Trigger:
.trigger(processingTime="5 seconds") makes sure the query runs every 5 seconds, so you'll see updated counts at that interval."""

query.awaitTermination()