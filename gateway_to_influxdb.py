#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import influx_writer


def parse_gateway_event(line):
    # Sample line: "2018-01-20T14:57:41Z WAN_DHCP 15524 2638 0"
    line_list = line.split(" ")

    if len(line_list) != 5:
        return None

    time = line_list[0]
    name = line_list[1]
    # format to milliseconds
    rtt = float(line_list[2]) / 1000
    rtt_sd = float(line_list[3]) / 1000
    packet_loss = float(line_list[4])

    json_body = [
        {'measurement': name, 'time': time, 'fields': {
            "RTT": rtt,
            "RTTsd": rtt_sd,
            "Packetloss": packet_loss
        }}
    ]
    return json_body


def main():
    try:
        influx_writer.send_events_to_influxdb(parse_gateway_event)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
