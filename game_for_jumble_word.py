# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:27:43 2026

@author: user
"""
import random

word = ["buchkadyat","bawalat","jhampya","pakau","dhenchu","jhandu","chirkut","chugli","phattu","pheku"]

c = 1
pp1 = 0
pp2 = 0
turn = 0

player1 = input("What is your name player1?")
player2 = input("What is your name player2?")

while(c == 1):
    def choice():
        
        return random.choice(word)
    pick_word = choice() #choose the random words

    def jumble(w):
        w = list(w)#list is convert string into the ['','','',''] form
        random.shuffle(w)#this is use to shuffle the list
        return ''.join(w)#join the list into a string
        
    J_W = jumble(pick_word)#jumble the random words
    
    if(turn%2 == 0):
        
        #player_1
        print(player1,J_W,"this is your jumble word")
        ans = input("What is the correct word of that jumble word?")
        
        if(ans == pick_word):
            pp1 = pp1 + 1
            turn = turn + 1
          
        else:
            print(player1,"correct word is",pick_word)
            C = input("press 1 to continue , 0 to finish/stop the game")
            turn = turn + 1
            c = int(C)
            
    
      
    else:
         #player_2
         print(player2,J_W,"this is your jumble word")
         ans = input("What is the correct word of that jumble word?")
         
         if(ans == pick_word):
             pp2 = pp2 + 1
             turn = turn + 1
           
         else:
             print(player2,"correct word is",pick_word)
             C = input("press 1 to continue , 0 to finish/stop the game")
             turn = turn + 1
             c = int(C)
             
print("game is over")        
print( player1,"your point is",pp1)
print( player2,"your point is",pp2)
            
    
    
    
    
    



