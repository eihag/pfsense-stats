#!/usr/bin/env bash
mosquitto_sub -h localhost -q 1 -t home/speedtest >>/opt/sensor/speedtest-event.log 2>>/opt/sensor/speedtest-client-error.log
