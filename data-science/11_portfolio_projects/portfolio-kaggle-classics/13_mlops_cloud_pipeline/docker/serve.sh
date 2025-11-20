#!/bin/bash
set -e

# Start nginx
nginx -c /etc/nginx/nginx.conf &

# Start Gunicorn
cd /app
exec gunicorn --bind unix:/tmp/gunicorn.sock \
              --workers 4 \
              --timeout 120 \
              --log-level info \
              --access-logfile - \
              --error-logfile - \
              inference:app
