# pfsense-stats
Collect various PFSense firewall statistics and send to mqtt queue


Steps:
1. Collect sample on pfsense firewall
2. Send from pfsense firewall to mqtt queue on Raspberry Pi
3. Send sample from Raspberry Pi to Influxdb
4. Visualize in Grafana dashboard



Statistics gathered:
* Packet loss (%)
* Round trip + standard deviation (ms)
* Internet capacity (MB/s) - using Speedtest 


## Install on pfsense firewall
1. enable ssh in web gui 
2. create new user for collecting stats, e.g. statsuser
3. Generate ssh key for statsuser and upload in web gui

### Install Mosquitto publisher on pfsense

<pre>
ssh firewall1 -l statsuser

sudo pkg add http://pkg.freebsd.org/freebsd:11:x86:64/latest/All/c-ares-1.12.0_2.txz
sudo pkg add http://pkg.freebsd.org/freebsd:11:x86:64/latest/All/mosquitto-1.4.14.txz
rehash
</pre>

### Collect gateway statistics on pfsense

<pre>
scp scripts/collect-gateway-stats.sh statsuser@firewall1:
ssh firewall1 -l statsuser
sh collect-gateway-stats.sh &

</pre>
(or add to startup script so it runs automatically after reboot)

### Collect speedtest statistics on pfsense
<pre>
scp scripts/collect-speedtest-stats.sh statsuser@firewall1:
ssh firewall1 -l statsuser
sh collect-speedtest-stats.sh &
</pre>

### Collect samples on remote MQTT server
Using a raspberry pi
<pre>
scp *.py rpi1:
scp scripts/*.sh rpi1:
scp config-gateway.properties rpi1:
ssh rpi1
sudo pip3 install influxdb
./start-gateway-eventlog.sh &
./start-gateway-influxdb-writer.sh & 
./start-speedtest-eventlog.sh &
./start-speedtest-influxdb-writer.sh &
</pre>
