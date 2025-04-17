# Upload the spark python file to GCS bucket
gsutil cp /home/chandrakarsatvik/consumer.py gs://satvik-storage-bucket/

# submit the Spark job to the Dataproc cluster
gcloud dataproc jobs submit pyspark gs://satvik-storage-bucket/consumer.py \
    --cluster=satvik-cluster \
    --region=us-west1 \
    --project=eminent-crane-448810-s3 \
    --jars=gs://satvik-storage-bucket/spark-sql-kafka-0-10_2.12-3.5.3.jar,gs://satvik-storage-bucket/kafka-clients-3.5.2.jar,gs://satvik-storage-bucket/spark-streaming-kafka-0-10_2.12-3.5.3.jar,gs://satvik-storage-bucket/spark-streaming-kafka-0-10-assembly_2.12-3.5.3.jar