# HOMEWORK 5 --- ES2
# Pendulum Simulation

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Sofia Levy
# NUMBER OF HOURS TO COMPLETE: 3
# YOUR COLLABORATION STATEMENT(s):
# Sofia Levy and Rene Jameson collaborated on this assignment.
# I received assistance from Dr. Cross on this assignment.
#*****************************************

import math
import numpy as np

#Global Variable Declarations
g = -9.8
L = 0.5

#Functions
def update_angular_time(t0, t1):
    dt = t1-t0
    return dt

def update_angular_pos(t0, t1, ang_pos0, ang_vel0):
    ang_position = ang_pos0 + (ang_vel0 * update_angular_time(t0, t1))
    return ang_position

def update_angular_vel(t0, t1, ang_acc, ang_vel0):
    angular_velocity = ang_vel0 + (ang_acc * update_angular_time(t0, t1))
    return angular_velocity

def update_angular_acc(ang_pos, ang_vel0, t0, t1):
    ang_acceleration = (g/L)*math.cos(((math.pi)/2) - update_angular_pos(t0, t1, ang_pos, ang_vel0))
    return ang_acceleration

#Initial Conditions
ang_time = np.linspace(0,10,10000)
ang_position = [math.pi/6]
ang_velocity = [0]
ang_acceleration = [0]
print(ang_time[0],ang_position[0],ang_velocity[0], ang_acceleration[0])

#Main Script
i = 1
while i < len(ang_time):
    # update position and velocity using previous values and time step
    ang_timeNext = update_angular_time(ang_time[i-1], ang_time[i])
    ang_posNext = update_angular_pos(ang_time[i-1], ang_time[i], ang_position[i-1], ang_velocity[i-1])
    ang_velNext = update_angular_vel(ang_time[i-1], ang_time[i], ang_acceleration[i-1], ang_velocity[i-1])
    ang_accNext = update_angular_acc(ang_position[i-1], ang_velocity[i-1], ang_time[i-1], ang_time[i])

    ang_position.append(ang_posNext)
    ang_velocity.append(ang_velNext)
    ang_acceleration.append(ang_accNext)

    print("Time: ", ang_time[i], " Angular position: ", ang_position[i], " Angular velocity:  ", ang_velocity[i], " Angular acceleration:  ", ang_acceleration[i])
    #print((ang_position[i],))
    i += 1