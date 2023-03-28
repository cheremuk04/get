import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        n = input()
        if n.isdigit():
            n = int(n)
            if n >= 0 and n<=255:
                GPIO.output(dac, decimal2binary(n))
                print(n/255 *3.3)
            else:
                print(("n should be  between 0 and 255"))
        elif n == "q":
            break
        else:
            print("n should be  between 0 and 255 or q")

except ValueError:
    print("n should be  between 0 and 255 or q")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()      

