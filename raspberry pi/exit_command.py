import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.cleanup()