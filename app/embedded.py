from app import app

# 全局变量
nowNum = 0
powerKey = '0'
leftKey = '0'
rightKey = '0'
upKey = '0'
downKey = '0'
# 模块

from flask import request
import time

# 获取来自前端的数据
@app.route("/myKey/", methods=['GET', 'POST'])
def myKey():
    global leftKey,rightKey,upKey,downKey
    leftKey = request.values['leftKey']
    rightKey = request.values['rightKey']
    upKey = request.values['upKey']
    downKey = request.values['downKey']
    return 'ok'




# 电源启动
@app.route("/powerType/", methods=['GET', 'POST'])
def powerType():
    loopFun(0.0001)
    return "ok"
    #         print('STOP')
    #         time.sleep(0.5)
        # if key == '1':
        #     stepper.runLeft(150)
        #     print("RUN")
        # else:


# from motosterFun import Stepper
from sensor import Sensor
# 循环函数
def loopFun(speed):
    global nowNum,powerKey,leftKey,rightKey,upKey,downKey
    powerKey = request.values['powerKey']
    # print("-----powerType事件触发------")
    # stepper = Stepper()
    sensor = Sensor()
    while powerKey == '1':
        # print("电源开启状态")
        if powerKey == '0':
            print("电源关闭")
            break
        time.sleep(speed)
        if leftKey == '1' and rightKey == '0' and upKey == '0' and downKey == '0':
            nowNum += 1
            print(nowNum)
            # stepper.runLeftOrRight('left')
            sensor.sensorCallback1()
        elif leftKey == '0' and rightKey == '1' and upKey == '0' and downKey == '0':
            nowNum -= 1
            print(nowNum)
            # stepper.runLeftOrRight('right')
        elif leftKey == '0' and rightKey == '0' and upKey == '1' and downKey == '0':
            # stepper.runUpOrDown('up')
            print("up")
        elif leftKey == '0' and rightKey == '0' and upKey == '0' and downKey == '1':
            # stepper.runUpOrDown('down')
            print('down')
        else:
            time.sleep(0.3)
            print("STOP")
