gcloud dataproc clusters create satvik-cluster \
    --region us-west1 \
    --zone us-west1-a \
    --single-node \
    --master-machine-type n1-standard-4 \
    --master-boot-disk-size 100GB \
    --image-version 2.2-debian12 \
    --project eminent-crane-448810-s3 \
    --initialization-actions=gs://satvik-storage-bucket/install_dependencies.sh