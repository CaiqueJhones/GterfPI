import RPi.GPIO as GPIO
import time
import sys

param = float(sys.argv[1])
SERVO = 18
VIBRADOR = 17

#GPIO config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(SERVO, GPIO.OUT) # Servo
GPIO.setup(VIBRADOR, GPIO.OUT) # Vibrador

p = GPIO.PWM(SERVO, 50)
p.start(0)

try:
	for x in range(0, 3):
		print "Executando vibracao"
		GPIO.output(VIBRADOR, GPIO.HIGH)
		time.sleep(3) # espera 3 segundos
		GPIO.output(VIBRADOR, GPIO.LOW)
		time.sleep(1) # espera 1 segundo
	
	print "Executando servo com " + str(param) + " segundos"
	p.ChangeDutyCycle(12.5) # turn towards 90 degree 12.5
	time.sleep(param) # espera de acordo com a vazao
	p.ChangeDutyCycle(0) # desliga o servo
	print "Fim de execucao"
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
