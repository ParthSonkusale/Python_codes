# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:04:01 2026

@author: user
"""

print("in the code we see your body mass intex (BMI)")
Weg = int(input("enter you weight:- "))
Hei = int(input("enter you height:- "))



bmi = Weg/(Hei*Hei)

if bmi <= 18.5:
    print("you are in Underweight")
elif bmi <= 25:
    print("your weight is normal ")
elif bmi <= 30:
    print("you are in overweight ")
else:
    print("you are obese")    
        
    