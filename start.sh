#!/bin/bash
python kernel-server.py &
lt --port 80 &

echo "Hello"

while true
do
    echo "Running..."
    sleep 60s
done
