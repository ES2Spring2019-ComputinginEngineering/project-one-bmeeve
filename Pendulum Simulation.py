#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:45:24 2019

@author: sofialevy
"""
#Title: Project 1: Pendulum Simulation
#Authors: Sofia Levy and Rene Jameson
#Overview: This code uses the 5 pendulum lengths used in the real world data 
#collection in order to simulate a "perfect" pendulum. A main function called 
#run_system calls other functions to plot the 
#angular position vs time of each pendulum length, calculates the period of each pendulum length,
#and finally graph the relationship between period vs pendulum length.

#Import statements
import math
import numpy as np
import scipy.signal as spy
import matplotlib.pyplot as plt

#Global Variable Declarations and Initial Conditions
g = -9.8
length_list = [0.17, 0.28, 0.42, 0.48, 0.61,]
period_list = []
ang_time = np.linspace(0,10,30000)
ang_position = [math.pi/2]
ang_velocity = [0]
ang_acceleration = [0]

#Sub-functions
def update_angular_time(t0, t1):  #returns the change in time
    dt = t1-t0
    return dt

def update_angular_pos(t0, t1, ang_pos0, ang_vel0):  #returns the angular position of simulated data
    ang_position = ang_pos0 + (ang_vel0 * update_angular_time(t0, t1))
    return ang_position

def update_angular_vel(t0, t1, ang_acc, ang_vel0):  #returns the angular velocity of simulated data
    angular_velocity = ang_vel0 + (ang_acc * update_angular_time(t0, t1))
    return angular_velocity

def update_angular_acc(ang_pos, ang_vel0, t0, t1, L):  ##returns the angular acceleration of simulated data
    ang_acceleration = (g/L)*math.cos(((math.pi)/2) - update_angular_pos(t0, t1, ang_pos, ang_vel0))
    return ang_acceleration

def plot_position(ang_time, ang_position):  #plots time on x-axis and angular position on y-axis
    #Plotting simulation data
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Position (m)')
    plt.title('Angular Position vs Length')
    plt.plot(ang_time, ang_position, 'r-')
    plt.grid()
    plt.show()
    
def calculate_period(ang_position): #calculates the peaks of the simulated data of angular position
    peaks_list = spy.find_peaks(ang_position)
    peak_points = ang_time[peaks_list[0]]
    
    time_period = np.diff(peak_points)
    period = np.sum(time_period)/len(time_period)
    print("The period is: " + str(period) + " seconds.")
    return period

def plot_len_v_per(length_list, period_list):  #plots the relationship between length of a pendulum and period
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.title('Period vs Length')
    plt.plot(length_list, period_list, 'b-')
    plt.grid()
    plt.show()

def plot_loglog(length_list, period_list):  #plots plots the relationship between length of a pendulum and period in a log-log graph
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.title('Period vs Length (Log-Log)')
    plt.plot(length_list, period_list, 'ro-')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid()
    plt.show()
    
#Main function
def run_system(L):  #runs a simulation of a pendulum, plots time vs. angular position, calculates the period of each length, plots length vs. period, and plots length vs. period in a log-log graph
    i = 1
    ang_time = np.linspace(0,10,30000)
    ang_position = [math.pi/2]
    ang_velocity = [0]
    ang_acceleration = [0]
    while i < len(ang_time):
        # update position and velocity using previous values and time step
        ang_timeNext = update_angular_time(ang_time[i-1], ang_time[i])
        ang_posNext = update_angular_pos(ang_time[i-1], ang_time[i], ang_position[i-1], ang_velocity[i-1])
        ang_velNext = update_angular_vel(ang_time[i-1], ang_time[i], ang_acceleration[i-1], ang_velocity[i-1])
        ang_accNext = update_angular_acc(ang_position[i-1], ang_velocity[i-1], ang_time[i-1], ang_time[i], L)
    
        ang_position.append(ang_posNext)
        ang_velocity.append(ang_velNext)
        ang_acceleration.append(ang_accNext)
    
        i += 1

    plot_position(ang_time, ang_position)
    
    period_list.append(calculate_period(ang_position))
    
#Main Script
for i in length_list:  #goes through each length in length_list
    print("\nPendulum length: " + str(i))
    run_system(i)
    
plot_len_v_per(length_list, period_list)
plot_loglog(length_list, period_list)
    
