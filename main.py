#!/usr/bin/env pybricks-micropython
#Importing libraries
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Defining variables
hand_motor = Motor(Port.A)
dispenser_motor = Motor(Port.B)
nose_motor = Motor(Port.C)
button = TouchSensor(Port.S2)
spider_eye = UltrasonicSensor(Port.S1)
degree=0

#Moving arm to initial position
hand_motor.run_target(500,90)

#Infinite loop
while True:
    distance = spider_eye.distance(False)
    #If something approaches sensor
    if distance <= 2000:
        #Arm moves
        print("Turn 1")
        hand_motor.run_target(500,-90)
        wait(1000)
        print("Turn 2")
        hand_motor.run_target(500,90)
        wait(500) 
        #Nose spins
        nose_motor.run_target(500,360)
        brick.sound.file(SoundFile.LAUGHING_1)
        nose_motor.run_target(500,0)
        wait(1500)
    
    #If button pressed
    if button.pressed():
        #Dispenser rotates, drops candy
        degree = degree + 45
        dispenser_motor.run_target(500,degree)
