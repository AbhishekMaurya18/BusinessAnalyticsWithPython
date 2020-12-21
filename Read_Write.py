# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:28:49 2020

@author: Abhishek Maurya
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('F:/pyWork/pyData/User_Data.csv')
df

# Writing CSV Files with Pandas:
df.to_csv('F:/pyWork/pyData/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('F:/pyWork/pyData/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
df1

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
df2
