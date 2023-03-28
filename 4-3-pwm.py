import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup([2], GPIO.OUT)
p = GPIO.PWM(2, 10000)
p.start(0)
try:
    while True:
        i = float(input())
        p.ChangeDutyCycle(i)

finally:
    p.stop()
    GPIO.cleanup()