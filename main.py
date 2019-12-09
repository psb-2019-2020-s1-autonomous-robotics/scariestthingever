#!/usr/bin/env pybricks-micropython

#Spooky Candy Robot
#By Jasmine Li and Maddy Malloy

'''
Want to get candy? Too bad, you'll have to 'git' past the monster in the screen first! This spooky robot scares you when you get too close, and dispenses candy if you're brave enough to push the button.
'''

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
brick.light(Color.RED)

#Infinite loop
while True:
    distance = spider_eye.distance(False)
    #If something approaches sensor
    if distance <= 2000:
        #Arm moves
        hand_motor.run_target(500,-90)
        wait(500)
        hand_motor.run_target(500,90)
        wait(500) 
        #Nose spins
        nose_motor.run_target(500,360)
        brick.sound.file(SoundFile.LAUGHING_1)
        nose_motor.run_target(500,0)
    
    brick.light(Color.GREEN)

    #Checks for button press for 500 ms
    i = 0
    while i<50:
        if button.pressed():
            #Dispenser rotates, drops candy
            degree = degree + 45
            dispenser_motor.run_target(500,degree)
            while button.pressed():
                wait(10)
            break
        else:
            wait(10)
            i += 10
    print(i)
    brick.light(Color.RED)
