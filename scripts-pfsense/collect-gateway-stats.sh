#!/usr/bin/sh
DPINGER_SOCK=`ls /var/run/dpinger*.sock`
MOSQUITTO_HOSTNAME=rpi1
MOSQUITTO_QUEUE=home/gateway

while true
do
    mosquitto_pub -h $MOSQUITTO_HOSTNAME -t $MOSQUITTO_QUEUE --qos 1 -m "`date -u +%Y-%m-%dT%H:%M:%SZ` `cat $DPINGER_SOCK`"
    sleep 5
done