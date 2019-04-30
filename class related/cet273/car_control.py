import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def go():
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(14, True)
    GPIO.output(15, False)

def back():
    GPIO.output(3, True)
    GPIO.output(2, False)
    GPIO.output(15, True)
    GPIO.output(14, False)

def left():
    GPIO.output(3, True)
    GPIO.output(2, False)
    GPIO.output(14, True)
    GPIO.output(15, False)

def right():
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(15, True)
    GPIO.output(14, False)

def stop():
    GPIO.output(2, False)
    GPIO.output(3, False)
    GPIO.output(14, False)
    GPIO.output(15, False)

if __name__ == '__main__':
    stop()
    while 1:
        command = input("please tell me waht i should do:")
        if command == 'go':
            go()
        elif command == 'back':
            back()
        elif command == 'left':
            left()
        elif command == 'right':
            right()
        elif command == 'stop':
            stop()
        elif command == 'exit':
            break
    GPIO.cleanup()