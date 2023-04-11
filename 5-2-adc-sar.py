import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka , GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def ToBin(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, ToBin(k))
        sleep(0.05)        
        if GPIO.input(comp) == 0:
            k -= 2**i
    return k

try:
    while True:
        k = adc()
        if k!=0:
            print(k, '{:.2f}v'.format(3.3*k/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()