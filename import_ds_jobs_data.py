#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:27:58 2021

@author: davidhinton
"""

#Pulled .csv file from 
from urllib.request import urlretrieve
import pandas as pd

url = 'https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/glassdoor_jobs.csv'

urlretrieve(url, 'glassdoor_jobs.csv')
df = pd.read_csv('glassdoor_jobs.csv')
print(df.head(15))