#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:24:51 2019

@author: sofialevy
"""
#Title: Project 1: micro:Bit Data Collection
#Authors: Sofia Levy and Rene Jameson
#Overview: This code is used to collect acceleration values from the micro:Bit,
#calculate the angular position at each time, and save those angular position 
#values to a data file.

#Import statements
import math
import microbit
import random 

#Global variables
list_accel_x = []
list_accel_y = []
list_time = []

filename = "data_" + str(random.randint(1, 999)) + ".txt" #creates a file to store microbit data

#Main script
while True:
    if microbit.button_a.is_pressed() == True: #checks to see if button a is pressed
        with open(filename, 'w') as pendulum_data:
            time0 = 0 #initiates first time value
            time0 = microbit.running_time() #sets time0 equal to the time the button is pressed
            while True:
                time1 = microbit.running_time() #initiates final time value 
                microbit.display.show(microbit.Image.HAPPY) #displays a happy face while button a is pressed
                elapsed_time = time1 - time0 #calculates difference in milliseconds
                elapsed_time_seconds = elapsed_time/1000 #calculates the time elapsed in seconds
                elapsed_time_seconds = str(elapsed_time_seconds) 
                
                x = microbit.accelerometer.get_x() #gets the acceleration in x-axis
                y = microbit.accelerometer.get_y() #gets the acceleration in y-axis

                a_y = str(math.atan2(y, x)) #calculates position of y
                a_x = str(math.atan2(x, y)) #calculates position of x
                    
                writestring = "Time: " + elapsed_time_seconds + ", Angular position X: " + a_x + ", Angular position y: " + a_y + ",\n"
                pendulum_data.write(writestring) #saves the time elapsed values, angular position x-axis values, and angular position y-axis values to a data.txt file
                    
                elapsed_time = 0 #resets elapsed_time
                elapsed_time_seconds = 0 #resets elapsed_time_seconds
                   
                microbit.sleep(50)

                if microbit.button_b.is_pressed() == True:
                    microbit.display.show(microbit.Image.SAD) #displays a sad face while button a is pressed
                    pendulum_data.close() #closes data file
                    break
