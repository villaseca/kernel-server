#!/bin/bash
node kernel-server.js &
lt --port 80 &

while true
do
    echo "Running..."
    sleep 60s
done
