# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:42:42 2026

@author: user
"""

import random
import datetime # this library for python to identify the calender (year-month-day)
 
birthday = []
i = 0
while(i <= 50):
    
    year = random.randint(1990,2020)
    if(year%4 == 0 and year%100!= 0 or year%400 == 0 ):
        leap = 1
    else:
        leap = 0
    
    months = random.randint(1,12)
    if(months == 2 and leap == 1):
        day = random.randint(1,29)
    elif(months == 2 and leap == 0):
        day = random.randint(1,28)
    elif(months == 4 or months == 6):
        day = random.randint(1,30)
    elif(months == 9 or months == 11):
        day = random.randint(1,30)
    elif(months%2 == 0 and months > 7):
        day = random.randint(1,31)
    else:
        day = random.randint(1,31)
        
    dd = datetime.date(year,months,day)
    day_of_year = dd.timetuple().tm_yday # this give the day from (1 to 365/366)
    i = i + 1
    birthday.append(day_of_year)
    
i = 0
while(i <= 50):
    birthday.sort()
    print(birthday[i])
    
    i = i + 1
     
        