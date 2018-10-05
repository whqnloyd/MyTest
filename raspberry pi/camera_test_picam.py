from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (640,480)
camera.framerate = 29

camera.start_preview()
sleep(20)
camera.close()