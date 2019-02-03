#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import logging
import datetime

logging.basicConfig(filename="monitor.log", level=logging.INFO)
logging.info("Started")


GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
RELAY_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

# Use Pin 18 for output (turn on and off)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)


def log_time():
    ts = time.time()
    dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    logging.info("Motion Detected at {}!!".format(dt))
    return dt


def MOTION(PIR_PIN):
    log_time()
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    log_time()


logging.info("PIR Module Test (CTRL+C to exit)?")
time.sleep(2)
logging.info("Ready?")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        logging.info("Sleeping for 100ms")
        time.sleep(100)
        logging.info("Back in action")
except KeyboardInterrupt:
    logging.info("Quit?")
    GPIO.cleanup()
