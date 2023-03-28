import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    p = int(input())
    while True:
        for i in range (256):
            GPIO.output(dac,decimal2binary(i))
            time.sleep(p/256)
        for i in range(255, 0, -1):
            GPIO.output(dac,decimal2binary(i))
            time.sleep(p/256)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()   