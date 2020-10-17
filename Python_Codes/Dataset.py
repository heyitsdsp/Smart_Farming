# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:53:27 2020

@author: bambo
"""
def get_data_details(loc):
    # IMPORT ALL NECESSARY MODULES
    import pandas as pd
    import numpy as np
    import os
    # PICK AND READ DATASET DYNAMICALLY 
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
    
    # FIX MORINGA ISSUE
    i = 0
    for i in range(0, len(table['Crop'])):
        if(table.Crop[i] == "Drumstick   moringa"):
            table.Crop[i] = "Drumstick"
        else:
            continue
    
    
    # INTERPOLATION USING NUMPY    
    table.N = table.N.astype('float64')
    for i in range(0, len(table.N)):
        table.N[i] = round(np.interp(table.N[i], [10, 180], [0, 1]), 1)
    
    table.P = table.P.astype('float64')
    for i in range(0, len(table.P)):
        table.P[i] = round(np.interp(table.P[i], [10, 125], [0, 1]), 1)
    
    table.K = table.K.astype('float64')
    for i in range(0, len(table.K)):
        table.K[i] = round(np.interp(table.K[i], [10, 200], [0, 1]), 1)
        
    # DELETE UNNAMED COLUMN
    table.drop(['Unnamed: 0'],axis=1,inplace=True)
    indexing_Crop = {}    
    
    # CREATE UNIQUE CROP TABLE
    uc_table = table.drop_duplicates(subset = 'Crop', keep = 'first')
    
    for index, value in uc_table.Crop.items():
        index = index + 1
        indexing_Crop[value] = index
        
    # UNIQUE INDEXING OF THE CROPS    
    for i in range(0, len(table.Crop)):
        for k in indexing_Crop.keys():
            if(table.Crop[i] == k):
                table.Crop[i] = indexing_Crop[k]    
    
    return [table, indexing_Crop]
#read FertPrediction dataset
loc_Fert = os.getcwd() + r'/Datasets/FertPredictDataset.csv'
data_Fert =pd.read_csv(loc_Fert)

#drop the column Ca,Mg,S,lime,C,Moisture
data_Fert.drop(['Ca','Mg','S','Lime','C','Moisture'],axis=1,inplace=True)

#drop class =1 row 
data_Fert.drop(data_Fert[data_Fert['class'] == 1].index, inplace = True) 

#Replace [2,3,4] to [1,2,3]
data_Fert["class"].replace({ 2 :  1, 3 : 2 , 4 : 3 }, inplace=True)


