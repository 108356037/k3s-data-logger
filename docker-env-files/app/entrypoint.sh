#!/bin/bash

/usr/local/bin/python -u /usr/src/app/run.py --customize=$WANT_CUSTOM --host=$MQTT_BROKER_SVC_PORT_1883_TCP_ADDR --port=$BROKER_PORT --topic=$PUBLISH_TOPIC --path=$PUBLISH_PATH  --freq=$FREQ