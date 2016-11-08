import RPi.GPIO as GPIO
import time
import sys

SERVO = 18

#GPIO config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SERVO, GPIO.OUT) # Servo

p = GPIO.PWM(SERVO, 50)
p.start(0)

try:
	p.ChangeDutyCycle(0) # desliga o servo
	print "Fim de execucao"
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
