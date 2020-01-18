import RPi.GPIO as GPIO
import time
from datetime import datetime

class Sensor():
   #霍尔传感器
    HALL = 31

    #霍尔传感器
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(HALL , GPIO.IN)

    # def change_detected(channel):
    #     # 如果检测到磁铁
    #     if GPIO.input(HALL) == GPIO.LOW:
    #         print 'Magnetic material detected: LED on'
    #     else:
    #     # 没检测到磁铁
    #         print 'No magnetic material: LED off'
    
    def sensorCallback1(channel):
      # Called if sensor output goes LOW
        # timestamp = time.time()
        # stamp = datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        # print("Sensor LOW " + stamp)
        myValue = GPIO.input(31)
        print(myValue)
    # GPIO.add_event_detect(HALL, GPIO.BOTH, change_detected, bouncetime=25)
    GPIO.add_event_detect(HALL, GPIO.FALLING, callback=sensorCallback1)