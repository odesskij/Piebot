#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import locals
import RPi.GPIO as GPIO


pygame.init()
pygame.joystick.init()  # main joystick device system
try:
    j = pygame.joystick.Joystick(0)  # create a joystick instance
    j.init()  # init instance
    print 'Enabled joystick: ' + j.get_name()
except pygame.error:
    print 'no joystick found.'
    exit()

# GPIO
MotorL = 16
MotorR = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MotorL, GPIO.OUT)
GPIO.setup(MotorR, GPIO.OUT)
while 1:
    event = pygame.event.wait()
    if event.type == locals.JOYHATMOTION:
        x, y = event.value
        # print x
        # print y
        # print event
        if x == 0:
            GPIO.output(MotorR, GPIO.LOW)
        if y == 0:
            GPIO.output(MotorL, GPIO.LOW)
        if x > 0:
            GPIO.output(MotorR, GPIO.HIGH)
        if y > 0:
            GPIO.output(MotorL, GPIO.HIGH)
        if x < 0:
            GPIO.output(MotorR, GPIO.HIGH)
        if y < 0:
            GPIO.output(MotorL, GPIO.HIGH)

            # x=1 right motor forward
            # y=1 left motor forward
            # x=-1 right motor backward
            # y=-1 left motor backward
