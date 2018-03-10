#!/usr/bin/sh
MOSQUITTO_HOSTNAME=rpi1
MOSQUITTO_QUEUE=home/speedtest

while true
do
    mosquitto_pub -h $MOSQUITTO_HOSTNAME -t $MOSQUITTO_QUEUE --qos 1 -m "`speedtest --json`"
    sleep 3600
done
