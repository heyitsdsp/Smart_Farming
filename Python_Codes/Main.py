# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:53:22 2020

@author: bambo
"""
# PREPARE STRINGS FOR STATEMENT
#==============================================================================
low_potassium = "\nThe amount of potassium in your soil is low! We recommend using a class 1 fertiliser to improve your soil condition to grow the best crops for the season!"
                
low_nitrogen = "\nThe nitrogen content of your soil is low! We recommend using a class 2 fertiliser to improve your soil condition to make the most of your field!"
                
low_phosphorous = "\nThe phosphorous content in your soil is low! We recommend using a class 3 fertiliser to improve your soil quality to get the best out of your field!"
#==============================================================================
                    
import Sensor_values as sv
import Crop_Pred as cp
import Fertiliser_Prediction as fp
import numpy as np

# GET THE SENSOR VALUES INTO THE CODE
sensor_values = sv.get_readings()
user_location = sensor_values[0]
sensor_values = sensor_values[1]

# CROP AND FERTILISER PREDICTION
#================================================================
# KNP FOR FERTILISER PREDICTION
Fertiliser_Input = np.array(sensor_values[1 : 4])

# NPK & pH FOR CROP PREDICTION
crop_input = sensor_values[0:4]
temp = crop_input[0]
for i in range(0, len(crop_input)-1):
    crop_input[i] = crop_input[i+1]

crop_input[len(crop_input)-1] = temp
    
# FINAL CROP PREDICTION
crop = cp.Predict_Crop(crop_input)
keys = list(crop[1].keys())
values = list(crop[1].values())

for i in range(0, len(values)):
    if(int(crop[0]) == i):
        crop_name = keys[i]

print("\nThe crop you should grow to get the most out of your field is ", 
      crop_name)

fertiliser = int(fp.Predict_Fertiliser([Fertiliser_Input]))

if(fertiliser == 1):
    print(low_potassium)
elif(fertiliser == 2):
    print(low_nitrogen)
else:
    print(low_phosphorous)
#================================================================


# WEATHER STATION (HARDCODED)
#================================================================
temp = sensor_values[4]
humidity = sensor_values[5]
pressure = sensor_values[6]

if(humidity > 70):
    print("\nIt's likely to rain today!")
elif(pressure < 100 and humidity > 70):
    print("\nHigh chances of a thunderstorm! Stay safe!")
elif(pressure < 99):
    print("\nStrong winds headed your way!")
else:
    print("\nThe weather is clear today!")
#================================================================
    


