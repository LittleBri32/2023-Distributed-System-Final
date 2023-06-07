#!/bin/sh
python3 /code/service4.py &
envoy -c /etc/service-envoy.yaml --service-cluster "service${SERVICE_NAME}"
