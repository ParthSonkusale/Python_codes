# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:28:01 2026

@author: user
"""

import random 

pack = []
comb = []    
i = random.randint(1,100)
if i % 2 == 0:
    even_number = i
    
    while True:
            prime_0 = True
            for num in range(2,100):
                for i in range(2, num):
                    if num % i == 0:
                        prime_0 = False
                        break
                    
                if prime_0:
                        
                    prime_1 = even_number - num
                    print("Checking:", num, prime_1)
                    while True:
                        prime = True
                        for j in range(2, prime_1):
                            if prime_1 % j == 0:
                                if j == (prime_1 - 1):
                                    prime = False
                                else:
                                    prime = True
                                break
                            
                        if prime:
                            pair = ([min(num, prime_1), max(num, prime_1)])  
                            if pair not in comb:
                                comb.append(pair)                       
                            break    
                    print("Final comb:", comb)
           
else:
    print("run one again")
