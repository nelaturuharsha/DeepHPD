import RPi.GPIO as GPIO
import time
from Inference.py import *

string = get_classifications()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
print "LED on"
if(string == 'human'):
  GPIO.output(7,GPIO.HIGH)
else:
    time.sleep(1)
print "LED off"
GPIO.output(7,GPIO.LOW)
