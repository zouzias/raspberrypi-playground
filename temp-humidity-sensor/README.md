# Humidity and Temperature using Raspberry Pi

Home sensor for temperature and humidity.

## Hardware parts

* Raspberry Pi 3 Model B+
* [DHT11 Digital Temperature and Humidity Sensor](https://www.adafruit.com/product/386)

## Setup

You need to install the AdaFruit DHT python package first

### Installation steps

```bash
sudo apt-get install git-core
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get install build-essential python-dev
sudo python setup.py install
```

### Periodically sample humidity/temperature

```bash
./temp-humidity-sensor.py
```


## Run long-standing process with supervisord

Add the following config and restart `supervisord`

```
cat /etc/supervisor/conf.d/temp-humidity-python.conf
[program:temp_humidity_sensor]
command=/home/pi/temp-humidity-sensor.py
autostart=true
autorestart=true
stderr_logfile=/var/log/temp-humidity-sensor.err.log
stdout_logfile=/var/log/temp-humidity-sensor.out.log
```
