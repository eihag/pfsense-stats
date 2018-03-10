#!/usr/bin/env bash
mosquitto_sub -h localhost -t home/gateway --qos 1|python3 ~/gateway_to_influxdb.py