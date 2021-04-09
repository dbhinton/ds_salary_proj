#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:07:30 2021

@author: davidhinton
"""

 
import glassdoor_scraper as gs
import pandas as pd

path = '/Users/davidhinton/Documents/ds_salary_proj/chromedriver'

df = gs.get_jobs('data scientist', 15, False, path, 15)