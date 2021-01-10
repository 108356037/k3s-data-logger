#!/bin/bash

export PYTHON_EXE=$(which python3)

$PYTHON_EXE -u /usr/src/app/run.py --host=$BROKER_IP --port=$BROKER_PORT --topic=$PUBLISH_TOPIC --path=$PUBLISH_PATH  --freq=$FREQ --client_id=$CLIENT_ID --username=$USERNAME --userpw=$USERPW