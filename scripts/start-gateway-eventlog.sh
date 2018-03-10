#!/usr/bin/env bash
mosquitto_sub -h localhost -q 1 -t home/gateway >>/opt/sensor/gateway-event.log 2>>/opt/sensor/gateway-client-error.log
