# Create a Kafka Topic (in another terminal)
cd kafka
bin/kafka-topics.sh --create --topic input-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1