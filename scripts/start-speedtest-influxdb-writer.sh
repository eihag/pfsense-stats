#!/usr/bin/env bash
mosquitto_sub -h localhost -t home/speedtest --qos 1|python3 ~/speedtest-to-influxdb.py