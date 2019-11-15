#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
handmotor = Motor(Port.A)
motor=Motor(Port.B)
nosemotor=Motor(Port.C)
Button=TouchSensor(Port.S2)
spidereye = UltrasonicSensor(Port.S1)
handmotor.run_target(500,90)
degree=0
while True:
    distance = spidereye.distance(False)
    print(distance)
    if distance <= 2000:
        #Arm code
        print("Turn 1")
        handmotor.run_target(500,-90)
        wait(1000)
        print("Turn 2")
        handmotor.run_target(500,90)
        wait(500) 
        #Nose code
        nosemotor.run_target(500,360)
        brick.sound.file(SoundFile.LAUGHING_1)
        nosemotor.run_target(500,0)
        wait(1500)
    if Button.pressed():
        #Dispenser code
        degree=degree+45
        motor.run_target(500,degree)


    
