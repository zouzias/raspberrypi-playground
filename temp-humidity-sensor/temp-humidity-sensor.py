#!/usr/bin/env python3
import Adafruit_DHT
import logging
import time
import datetime
import json

logging.basicConfig(filename="/var/log/temp-humidity-sensor.log", level=logging.INFO)


def log_values(humidity, temperature):
    """Log sensor values"""
    ts = time.time()
    dt = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    item = {"timestamp": dt, "temperature": temperature, "humidity": humidity}
    logging.info(json.dumps(item))
    print(
        "[{}]Temp: {0:0.1f} C  Humidity: {1:0.1f} %".format(dt, temperature, humidity)
    )
    return dt


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor's value to be
# connected to GPIO17.
pin = 17

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    log_values(humidity, temperature)
    time.sleep(60)  # sample every 60 seconds
