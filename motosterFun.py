import RPi.GPIO as GPIO
import time


# 有效
class Stepper:
    # 控制旋转角度
    power = 36
    fang = 38

    # # 控制上下
    power2 = 33
    fang2 = 35

    stepperLeftKey = '0'
    stepperRightKey = '0'
    stepperUpKey = '0'
    stepperDownKey = '0'

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(power, GPIO.OUT)
    GPIO.setup(fang, GPIO.OUT)

    GPIO.setup(power2, GPIO.OUT)
    GPIO.setup(fang2, GPIO.OUT)
    # GPIO.setup(channel, GPIO.OUT)
    
    #指定值转动
    def runLeftOrRight(self,direction):
        if direction == 'left' and self.stepperLeftKey == '0':
            self.stepperLeftKey = '1'
            self.stepperRightKey = '0'
            self.stepperUpKey = '0'
            self.stepperDownKey = '0'
            GPIO.output(38, GPIO.HIGH)
            print('leftMotoer')
        elif direction == 'right' and self.stepperRightKey == '0':
            self.stepperLeftKey = '0'
            self.stepperRightKey = '1'
            self.stepperUpKey = '0'
            self.stepperDownKey = '0'
            GPIO.output(38, GPIO.LOW)
            print('rightMotoer')
        for i in range(0,100): 
            GPIO.output(self.power, GPIO.HIGH)
            time.sleep(0.0001) 
            GPIO.output(self.power, GPIO.LOW)
            time.sleep(0.0001)

    def runUpOrDown(self,direction):
        if direction == 'up' and self.stepperUpKey == '0':
            self.stepperLeftKey = '0'
            self.stepperRightKey = '0'
            self.stepperUpKey = '1'
            self.stepperDownKey = '0'
            GPIO.output(35, GPIO.HIGH)
        elif direction == 'down' and self.stepperDownKey == '0':
            self.stepperLeftKey = '0'
            self.stepperRightKey = '0'
            self.stepperUpKey = '0'
            self.stepperDownKey = '1'
            GPIO.output(35, GPIO.LOW)
        for i in range(0,100): 
            GPIO.output(self.power2, GPIO.HIGH)
            time.sleep(0.0005) 
            GPIO.output(self.power2, GPIO.LOW)
            time.sleep(0.0005)
    
  

    # def runLeft(self,rangeNum):
    #     # return 'left' 
    #     print("left")
    #     GPIO.output(fang, GPIO.HIGH)
    #     for i in range(0,rangeNum): 
    #         GPIO.output(power, GPIO.HIGH)
    #         time.sleep(0.0005) 
    #         GPIO.output(power, GPIO.LOW)
    #         time.sleep(0.0005)
    # def runRight(rangeNum):
    #     GPIO.output(fang, GPIO.LOW)
    #     for i in range(0,rangeNum):
    #         GPIO.output(power, GPIO.HIGH)
    #         time.sleep(0.0005) 
    #         GPIO.output(power, GPIO.LOW)
    #         time.sleep(0.0005) 

    # # 


    # def runTop(rangeNum):
    #     print('right')
    #     GPIO.output(fang2, GPIO.HIGH)
    #     for i in range(0,rangeNum): 
    #         GPIO.output(power2, GPIO.HIGH)
    #         time.sleep(0.0005) 
    #         GPIO.output(power2, GPIO.LOW)
    #         time.sleep(0.0005)
    # def runUnder(rangeNum):
    #     GPIO.output(fang2, GPIO.LOW)
    #     for i in range(0,rangeNum): 
    #         GPIO.output(power2, GPIO.HIGH)
    #         time.sleep(0.0005) 
    #         GPIO.output(power2, GPIO.LOW)
    #         time.sleep(0.0005) 