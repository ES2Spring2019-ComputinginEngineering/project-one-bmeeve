#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:58:57 2019

@author: sofialevy
"""
#Title: Project 1: Parsing file
#Authors: Sofia Levy and Rene Jameson
#Overview: This code will parse through the angular position data recorded for 
#each pendulum length and run a main function called run_system that plots the 
#angular position vs time of each pendulum length, plots the the filtered 
#angular position vs time of each pendulum length, calculates the period of each pendulum length,
#and finally graphs the relationship between period vs pendulum length.

#Import statements
import matplotlib.pyplot as plt
import math
import scipy.signal as sig
import numpy as np

#Global variable declarations
data_list = ['data_889.txt', 'data_723.txt', 'data_820.txt', 'data_907.txt', 'data_153.txt']
list_time = []
list_accel_x = []
list_accel_y = []
list_tilts = []
tilt_noisy_filt = []
tilt_noisy_filt_pks = []
period_list = []
length_list = [0.17, 0.28, 0.42, 0.48, 0.61,]

#Sub-functions
def plot_tilts(list_time, list_tilts):  #plots time vs angular poisition
    plt.figure()
    plt.xlabel('Time (seconds)')
    plt.ylabel('Angular Position (m)')
    plt.title('Angular Position vs Time')
    plt.plot(list_time, list_tilts, 'k-')
    plt.grid()
    plt.show()

def plot_noisy_median_filtered(time, tilts, tilt_noisy_filt, tilt_noisy_filt_pks):  #plots a filtered graph of time vs. angular position
    plt.figure()
    plt.xlabel('Time (seconds)')
    plt.ylabel('Angular Position (m)')
    plt.title('Angular Position vs Time')
    plt.plot(time, tilt_noisy_filt,'r-', time[tilt_noisy_filt_pks], 
             tilt_noisy_filt[tilt_noisy_filt_pks], 'b.')
    plt.title('Noisy Median Filtered Angular Position')
    plt.grid()
    plt.show()

def calculate_period(time, tilt_noisy_filt_pks):  #calculates the period of graph of angular position
    peak_points = time[tilt_noisy_filt_pks]
    
    time_period = np.diff(peak_points)
    period = np.sum(time_period)/len(time_period)
    print("The period is: " + str(period) + " seconds.")
    return period
    
def plot_len_v_period(length_list, period_list):  #plots length of pendulum vs. period of real world data
    plt.plot(length_list, period_list, 'bo-')
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.title('Period vs Length')
    plt.grid()
    plt.show()

def plot_loglog(length_list, period_list):  #plots length of pendulum vs. period of real world data on log-log graph
    #Plot of real world data periods vs lengths (log-log graph)
    plt.loglog(length_list, period_list, 'ro-')
    plt.xlabel('Length (m)')
    plt.ylabel('Period (s)')
    plt.title('Period vs Length (Log-Log)')
    plt.grid()
    plt.show()

#Main function
def run_system(data):  #runs and calls all functions in order to calculate the periods of real world data, plot time vs. angular position, and plot the relationship of length vs. period
   fin = open(data)
   list_time = []
   list_accel_x = []
   list_tilts = []
   
   for i in fin:
       split_i = i.split(',')
       list_time.append(float(split_i[0][6:]))
       list_accel_x.append(float(split_i[1][25:]))

       list_tilts = list_accel_x 
   
   time = np.array(list_time) #converts list of times in array

   plot_tilts(time, list_tilts)
   
   tilts = np.array(list_tilts) #converts list of positions into array
   
   tilt_noisy_filt = sig.medfilt(list_tilts, 7) #median filter for angular position data

   tilt_noisy_filt_pks, _ = sig.find_peaks(tilt_noisy_filt, prominence = 0.02)  #identifies the peaks of angular position data
   
   plot_noisy_median_filtered(time, tilts, tilt_noisy_filt, tilt_noisy_filt_pks)  
   
   period_list.append(calculate_period(time, tilt_noisy_filt_pks))  #creates a list of the determined periods for each pendulum length
   

#Main Script
j = 0
for i in data_list:  #runs through each data file for each pendulum length
    print("\nPendulum length: " + str(length_list[j]))
    run_system(i)
    j += 1

plot_len_v_period(length_list, period_list)  
plot_loglog(length_list, period_list)




