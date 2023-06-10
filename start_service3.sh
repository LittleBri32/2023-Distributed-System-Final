#!/bin/sh
python3 /code/service3.py &
envoy -c /etc/service-envoy.yaml --service-cluster "service${SERVICE_NAME}"
