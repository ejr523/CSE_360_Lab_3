from Motor import *            
PWM=Motor()          

from Ultrasonic import *
ultrasonic=Ultrasonic()

import time

def test3():
    try:
        data=ultrasonic.get_distance()
        k=75
        dist=data-50
        PWM.setMotorModel(k*dist, k*dist, k*dist, k*dist)
        start=time.time()
        while True:
            data=ultrasonic.get_distance()
            dist=data-50
            PWM.setMotorModel(k*dist, k*dist, k*dist, k*dist)
            print("Wall is " + str(data) + " CM away, " + "speed = " + str(k*dist) + ", time = " + str(time.time() - start))
    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("Program quit, ending distance was " + str(data) + " CM")

def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.get_distance()   #Get the value
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")

def forback():
    print("Moving robot forward at speed 1000")
    
    PWM.setMotorModel(1000,1000,1000,1000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot backward at speed 1000")
    PWM.setMotorModel(-1000, -1000, -1000, -1000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot forward at speed 2000")
    PWM.setMotorModel(2000,2000,2000,2000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot backward at speed 2000")
    PWM.setMotorModel(-2000,-2000,-2000,-2000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot forward at speed 3000")
    PWM.setMotorModel(3000,3000,3000,3000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot backward at speed 3000")
    PWM.setMotorModel(-3000,-3000,-3000,-3000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot forward at speed 4000")
    PWM.setMotorModel(4000,4000,4000,4000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
    print("Moving robot backward at speed 4000")
    PWM.setMotorModel(-4000,-4000,-4000,-4000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)
    
if __name__ == '__main__':
    test3()