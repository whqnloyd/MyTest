import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import car_control

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xA1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x60)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()

while(1):
    # ackPL = [1]
    while not radio.available(0):
        time.sleep(1 / 100)
    msg = []
    radio.read(msg, radio.getDynamicPayloadSize())
    print("Received: ",msg)
    
    #car_control.stop()
    if msg[0] == 1:
        if msg[2] >= 70:
            car_control.go()
        elif msg[2] <= 30:
            car_control.back()
        elif msg[4] >= 70:
            car_control.right()
        elif msg[4] <= 30:
            car_control.left()
    elif msg[0] == 0:
        car_control.stop()
    #elif command == 'exit':
    #    break
    #GPIO.cleanup()
    
    '''
    print("Translating the receivedMessage into unicode characters")
    string = ""
    for n in receivedMessage:
        # Decode into standard unicode set
        if (n >= 32 and n <= 126):
            string += chr(n)
    print("Out received message decodes to: {}".format(string))
    '''
