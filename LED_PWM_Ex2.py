#git clone https://github.com/Majdawad88/LED_PWM_Ex2.git

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LED = 21
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        numBlinks = int(input('Enter Number of Blinks: '))
        delayOn = float(input('Enter DelayOn: '))
        delayOff = float(input('Enter DelayOff: '))

        for i in range(numBlinks):
            GPIO.output(LED, GPIO.HIGH)
            print('LED ON')
            sleep(delayOn)
            GPIO.output(LED, GPIO.LOW)
            print('LED OFF')
            sleep(delayOff)
except KeyboardInterrupt:
    print('\nExiting...')
finally:
    GPIO.cleanup()
