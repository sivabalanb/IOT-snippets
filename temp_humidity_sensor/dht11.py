import sys
import RPi.GPIO as GPIO
import os
import Adafruit_DHT
import urllib2
import smbus
import time
from ctypes import c_short

DHTpin = 4
# Define GPIO to LCD mapping
def readDHT():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    return (str(int(humidity)), str(int(temperature)))

def postdata(URL, key, timeout):  
    while True:
        (humidity, temperature)= readDHT()
        finalURL = URL +"&field1=%s&field2=%s"%(humidity, temperature)
        thingspeakurl = urllib2.urlopen(finalURL);
        print(humidity+ " " + temperature + " ")
        thingspeakurl.close()
        time.sleep(timeout)
     
if __name__=="__main__":
    
    key="secretkey"       # Enter your Write API key from ThingSpeak
    GPIO.setmode(GPIO.BCM)
    URL = 'https://api.thingspeak.com/update?api_key=%s' % key
    timeout = 10
    postdata(URL, key, timeout)