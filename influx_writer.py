import configparser
import logging
import sys
import time

from influxdb import InfluxDBClient

from timeout import timeout

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

configFilePath = r'config-gateway.properties'


def send_events_to_influxdb(parser):
    logger.info("Starting up..")
    config_parser = configparser.ConfigParser()
    config_parser.read(configFilePath)
    config_section = config_parser['gateway']
    read_events(config_section, parser)


def non_blank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def read_events(config_section, parser):
    influxdb_client = get_influxdb_client(config_section, logger)

    logger.info("Listening for events")

    for line in non_blank_lines(sys.stdin):
        logger.info("Event received: {}".format(line))

        payload = parser(line)

        if payload is not None:
            logger.info("Write points: {0}".format(payload))
            write_influxdb(influxdb_client, payload, logger)


def get_influxdb_client(config_section, logger):
    logger.info("Using database: '{0}'".format(config_section['DATABASE']))
    return InfluxDBClient(config_section['HOSTNAME'],
                          config_section['PORT'],
                          config_section['USER'],
                          config_section['PASSWORD'],
                          config_section['DATABASE'],
                          ssl=True, verify_ssl=True)


def write_influxdb(influxdb_client, payload, logger):
    while True:
        try:
            influx_http_call(influxdb_client, payload)
        except Exception as e:
            logger.exception(str(e))
            logger.exception("Error writing to InfluxDB. Retrying in 30sec")
            time.sleep(30)
            continue
        else:
            break


@timeout(30)
def influx_http_call(influxdb_client, payload):
    influxdb_client.write_points(payload)
