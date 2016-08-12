#!/bin/bash
python kernel-server.py &

echo "Hello"

while true
do
    echo "Running..."
    sleep 60s
done
