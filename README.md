## Task  
**Simulate a real-time streaming application using Kafka and Spark Streaming.**  
- Create a file with at least 1000 rows and upload it to a GCS bucket. 
- Write a producer that reads the file in batches of 10 records and sends them to a Kafka topic with a delay of 10 seconds between batches.
- Write a Spark Streaming consumer that reads from the same Kafka topic every 5 seconds and emits the count of rows seen in the last 10 seconds.

## Report  
- [View the PDF](/21f1000344-IBD-GA7.pdf)

## Video Presentation  
[![Watch the video](images/video-thumb.png)](https://drive.google.com/file/d/1ovmmLgjZxvjJOvX1GddVbE4biRVA1l_X/view?usp=sharing)

## Using Seperate Resources
- The above project has also been implemented using three seperate resources.
- Provisioned and configured three VMs: Kafka broker, producer, and Spark Streaming consumer.
- Producer creates a file with at least 1000 rows and upload it to a GCS bucket. It also reads the file in batches of 10 records and sends them to a Kafka topic with a delay of 10 seconds between batches.
- Spark Streaming consumer reads from the same Kafka topic every 5 seconds and emits the count of rows seen in the last 10 seconds.
- [View the project using seperate resources](/Using_Seperate_Resources)