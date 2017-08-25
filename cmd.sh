#!/bin/bash
set -e
if [ "$ENV" = "DEV" ]; then
	echo "Running development server"
	exec python /app/identidock.py
elif [ "$ENV" = "TEST" ]; then
    echo "Running unit tests"
    exec python /app/test.py
else
	echo "Running production server"
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9091
fi
