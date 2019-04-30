import RPi.GPIO as GPIO      #load lib

GPIO.setmode(GPIO.BCM)		#setup mode
GPIO.setup(2, GPIO.OUT)		#set pin 2 as output pin, so controller can use it output signal
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

def go():					#go() function, it include commands for each pin
    GPIO.output(2, True)	#set pin 2 as HIGH
    GPIO.output(3, False)	#set pin 3 as LOW
    GPIO.output(4, True)
    GPIO.output(5, False)

def back():
    GPIO.output(3, True)
    GPIO.output(2, False)
    GPIO.output(5, True)
    GPIO.output(4, False)

def left():
    GPIO.output(3, True)
    GPIO.output(2, False)
    GPIO.output(4, True)
    GPIO.output(5, False)

def right():
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(5, True)
    GPIO.output(4, False)

def stop():
    GPIO.output(2, False)
    GPIO.output(3, False)
    GPIO.output(4, False)
    GPIO.output(5, False)

if __name__ == '__main__':
    command = input("please tell me waht i should do:")		#set the interface for user
    while 1:												#loop
        if command == 'go':									#check the command from input 
            go()
        elif command == 'back':
            back()
        elif command == 'left':
            left()
        elif command == 'right':
            right()
        elif command == 'stop':
            stop()
        elif command == 'exit':								#exit the loop
            break
    GPIO.cleanup()											#clean the pin setup, or you will get a warning next time when you run the program