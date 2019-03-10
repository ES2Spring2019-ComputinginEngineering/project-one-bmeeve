#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:51:36 2019

@author: sofialevy
"""
# Project 1 ES2 
## Project Description
The purpose of this project was to determine the relationship between pendulum 
length and period of oscillation. To begin, real world acceleration data was 
collected using a microbit. The file **microbit_data_collection.py** contains 
the code to collect acceleration data from a microbit and calculate the 
angular position and correlated elapsed time and save this data to a text file 
for five different pendulum lengths. Next, the data collected was used to calculate 
the period of oscillation. The file **parsing.py** contains the code to graph 
the angular position vs. time for each 5 lengths, graph the filtered 
data for angular position vs. time, calculate the period of each 
length, graph the relationship of period vs. pendulum length, and finally graph
the relationship between period vs pendulum length in a log-log graph. Finally, 
the same 5 lengths used to calculate the angular position and time for the 
real world data were used in a "perfect" physics simulation. The file 
**Pendulum_Simulation.py** contains the code to use the same 5 pendulum lengths 
from the real world data collection to graph the angular position vs. time, 
caclulate the period for each length, graph the period vs. pendulum length for
all 5 lengths, and finally create a log-log graph for the period vs. 
pendulum length for all 5 lengths. The data for period of oscillation and 
graphs of period vs. pendulum length for the real world data collection and 
simulation can then be compared to determine and analyze the relationship 
between period of oscillation and pendulum length.
### Instructions for **microbit_data_collection.py**
**Link to file:** [microbit_data_collection.py] (https://github.com/ES2Spring2019-ComputinginEngineering/project-one-bmeeve/blob/master/microbit_data_collection.py)

Connect the micro:Bit to the laptop and flash the code onto the micro:Bit. 
pendulum. The place the micro:Bit with a battery onto the end of the pendulum.
Hold your pendulum at a 90 degree 
angle from its initial position hanging straight downwards
Press button A on your micro Bit and a smiley face 
should appear indicating data collection as begun. Release your pendulum with 
the microBit let the pendulum swing to collect data. When the data collection 
is complete and the pendulum stops swinging, or when you would like to stop 
data collection, press button B on your micro:Bit and a frowning face should 
appear indicating the data collection has stopped. A file will be created on 
your computer by the program with a name 
“data_(random number from 1 to 999).text.” Open this file on your computer 
to access the data collected by your micro Bit including time elapsed in 
seconds, angular position using x, and angular position y of the pendulum’s 
swinging motion. 5 data.txt files have already been collected for this project
and will be used for the **parsing.py** file. 

```
This code will be used to calculate the angular position of the pendulum based on the x-axis:

x = microbit.accelerometer.get_x() 
y = microbit.accelerometer.get_y() 

a_y = str(math.atan2(y, x)) #calculates position of y
a_x = str(math.atan2(x, y)) #calculates position of x

```
**IMPORTANT NOTE:** The graphs of both angular position on the x-axis and angular position on the y-axis were graphed
and it was determined that the graph using the x-axis should be used for calculations of period oscillation.

### Instructions for **parsing.py**
**Link to file:** [parsing.py] (https://github.com/ES2Spring2019-ComputinginEngineering/project-one-bmeeve/blob/master/parsing.py)

Click the run button. The code should automatically use the 5 data.txt files
collected from the microbit in order to output each angular position vs. time 
graph and each period vs. pendulum length graph. The first output should include
printed length of the pendulum, the graph of the angular position vs. time,
the graph of the filtered angular position vs. time, and the printed 
period calculation. Lastly, the output should include a graph of the calculated
periods vs. pendulum length and a graph of the calculated
periods vs. pendulum length in a log-log graph.

```
This code will be used to calculate the period of oscillation:

peak_points = time[tilt_noisy_filt_pks]
    
    time_period = np.diff(peak_points)
    period = np.sum(time_period)/len(time_period)
```
### Instructions for **Pendulum_Simulation**
**Link to file:** [Pendulum_Simulation.py] (https://github.com/ES2Spring2019-ComputinginEngineering/project-one-bmeeve/blob/master/Pendulum%20Simulation.py)

Click the run button. The code should automatically use the list of the 5 real world lengths
collected from the microbit in order to output each angular position vs. time 
graph and each period vs. pendulum length graph. The first output should include
printed length of the pendulum, the graph of the angular position vs. time, 
and the printed 
period calculation. Lastly, the output should include a graph of the calculated
periods vs. pendulum length and a graph of the calculated
periods vs. pendulum length in a log-log graph.