# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:51:39 2020

@author: bambo
"""

def get_readings():    
    import ipinfo
    import random
    
    # Using your IP Address to find out your location
    
    ipinfo_api_key = (input('Enter the API Key : '))
    handler = ipinfo.getHandler(ipinfo_api_key)
    details = handler.getDetails()
    city = details.city
    
    # Generation of random values for circuit simulation
    
    Artificial_pH = round(random.uniform(2,12), 2)
    Artificial_N = round(random.normalvariate(0.551782, 0.209015), 2)
    Artificial_P = round(random.normalvariate(0.550594, 0.203223), 2)
    Artificial_K = round(random.normalvariate(0.554283, 0.209547), 2)
    
    Artificial_Moisture = round(random.uniform(27,87), 2)
    Artificial_Pressure = round(random.uniform(98, 103), 2)
    
    Artificial_temp = round(random.uniform(25, 45), 2)
    Artificial_humidity = round(random.uniform(29, 90), 2)
    
    # Collating all random values in a list
    
    readings = [Artificial_pH, Artificial_N, Artificial_P, Artificial_K, 
                Artificial_temp, Artificial_humidity, Artificial_Pressure, 
                Artificial_Moisture]
    
    # Printing the values to know the order    
    print('pH : ', Artificial_pH)
    print('N : ', Artificial_N)
    print('P : ', Artificial_P)
    print('K : ', Artificial_K)
    print('Temperature : ', Artificial_temp)
    print('Humidity : ', Artificial_humidity)
    print('Pressure : ', Artificial_Pressure)
    print('Moisture : ', Artificial_Moisture)

    return [city, readings]

