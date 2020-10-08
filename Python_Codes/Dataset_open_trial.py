# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:53:27 2020

@author: bambo
"""

# IMPORT ALL NECESSARY MODULES
import pandas as pd
import numpy as np
import os
import re    

# PICK AND READ DATASET DYNAMICALLY 
loc = os.getcwd() + r'/Datasets/Crop_Pred.csv'
table = pd.read_csv(loc)

# DROP DUPLICATE RECORDS (IF ANY)
table = table.drop_duplicates(subset = None, keep = 'first')

# GETTING RID OF ALL UNNECESSARY SYMBOLS OR NAMES
spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
for char in spec_chars:
       table['Crop'] = table['Crop'].str.replace(char, ' ')
       table['Crop'] = table['Crop'].str.replace(r"\(.*\)","")

# FIX MORINGA ISSUE IN A COMPLICATED MANNER
"""def moringa(crop_name):
    pattern = re.compile(r'(Drumstick)')
    drumsticks = re.findall(pattern, crop_name)
    new_name = "".join(drumsticks)
    return new_name

i = 0      

for crop in table['Crop']:
    if(crop == "Drumstick   moringa"):
        table['Crop'][i] = moringa(crop)
    i+=1
"""

# FIX MORINGA ISSUE IN A SIMPLE MANNER
"""i = 0
for i in range(0, len(table['Crop'])):
    if(table.Crop[i] == "Drumstick   moringa"):
        table.Crop[i] = "Drumstick"
    else:
        continue
"""

# SCALING USING NUMPY
for i in range(0, len(table.N)):
    table.N[i] = round(np.interp(table.N[i], [10, 180], [0, 1]), 2)
    
    
        
    