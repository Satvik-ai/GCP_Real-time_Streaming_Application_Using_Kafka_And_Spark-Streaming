# Download Jars
wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.2/kafka-clients-3.5.2.jar
wget https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.3/spark-sql-kafka-0-10_2.12-3.5.3.jar
wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.5.3/spark-streaming-kafka-0-10_2.12-3.5.3.jar
wget https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.12/3.5.3/spark-streaming-kafka-0-10-assembly_2.12-3.5.3.jar

# Upload the Jars to GCS Bucket
gsutil cp /home/chandrakarsatvik/consumer/spark-sql-kafka-0-10_2.12-3.5.3.jar gs://satvik-storage-bucket/
gsutil cp /home/chandrakarsatvik/consumer/kafka-clients-3.5.2.jar gs://satvik-storage-bucket/
gsutil cp /home/chandrakarsatvik/consumer/spark-streaming-kafka-0-10_2.12-3.5.3.jar gs://satvik-storage-bucket/
gsutil cp /home/chandrakarsatvik/consumer/spark-streaming-kafka-0-10-assembly_2.12-3.5.3.jar gs://satvik-storage-bucket/
