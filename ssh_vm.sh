#!/bin/bash

# Variables
ZONE="us-central1-a"
VM_NAME="kafka-spark-vm-2"

# SSH into the VM
gcloud compute ssh $VM_NAME --zone=$ZONE