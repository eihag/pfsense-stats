#!/usr/bin/env bash
#/usr/bin/pkill eventlog
/usr/bin/screen -d -m -S gateway-log bash ~/start-gateway-eventlog.sh
/usr/bin/screen -d -m -S speedtest-log bash ~/start-speedtest-eventlog.sh
/usr/bin/screen -d -m -S gateway-influxdb bash ~/start-gateway-influxdb-writer.sh
/usr/bin/screen -d -m -S speedtest-influxdb bash ~/start-speedtest-influxdb-writer.sh
