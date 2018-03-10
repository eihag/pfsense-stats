#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


import influx_writer


def parse_speedtest_event(line):
    try:
        json_input = json.loads(line)
    except ValueError:
        return None

    if 'timestamp' not in json_input \
            or 'download' not in json_input \
            or 'upload' not in json_input \
            or 'server' not in json_input \
            or 'ping' not in json_input:
        return None

    name = "Speedtest"
    time = json_input["timestamp"]
    dl_mbps = float("{:.2f}".format(float(json_input["download"]) / (1000 * 1000)))
    ul_mbps = float("{:.2f}".format(float(json_input["upload"]) / (1000 * 1000)))
    ping_ms = float(json_input["ping"])

    json_body = [
        {'measurement': name, 'time': time, 'fields': {
            "ul_mbps": ul_mbps,
            "dl_mps": dl_mbps,
            "ping_ms": ping_ms
        }}
    ]
    return json_body


def main():
    try:
        influx_writer.send_events_to_influxdb(parse_speedtest_event)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
