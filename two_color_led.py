import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    #close
    #GPIO.output(38, GPIO.LOW)
    #GPIO.output(40, GPIO.LOW)
    #time.sleep(1)
    #yellow
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.LOW)
    time.sleep(1)
    #red
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(1)
    #yellow merge red
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(1)
    
GPIO.cleanup()