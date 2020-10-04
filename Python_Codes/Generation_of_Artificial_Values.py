# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:51:39 2020

@author: bambo
"""
import ipinfo
import random

# Using your IP Address to find out your location

ipinfo_api_key = (input('Enter the API Key : '))
handler = ipinfo.getHandler(ipinfo_api_key)
details = handler.getDetails()
print(details.city)

# Generation of random values for circuit simulation

Artificial_pH = random.uniform(2,12)
Artificial_N = random.normalvariate(0.551782, 0.209015)
Artificial_P = random.normalvariate(0.550594, 0.203223)
Artificial_K = random.normalvariate(0.554283, 0.209547)

Artificial_Moisture = random.uniform(0,100)

