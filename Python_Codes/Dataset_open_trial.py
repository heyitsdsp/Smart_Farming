# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:53:27 2020

@author: bambo
"""

import pandas as pd
import os
import re

loc = os.getcwd() + r'/Datasets/Crop_Pred.csv'
table = pd.read_csv(loc)

table = table.drop_duplicates(subset=['Crop','N','P','K','pH'], keep='first')




spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
for char in spec_chars:
       table['Crop'] = table['Crop'].str.replace(char, ' ')
       table['Crop'] = table['Crop'].str.replace(r"\(.*\)","")
       


