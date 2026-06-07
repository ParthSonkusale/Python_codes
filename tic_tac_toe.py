# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:25:38 2026

@author: user
"""
player1 = input("enter your name player1:- ")
player2 = input("enter your name player2:- ")
c = 1
TT = []
for i in range(3):
    T = []
    for j in range(3):
        T.append(0)
    TT.append(T)
    
while(c):
    #player1
    print(player1,"your symbol is X")
    i = int(input("enter row(0 or 1 or 2):- "))
    j = int(input("enter col(0 or 1 or 2):- "))
    TT[i][j] = "X"
    for i in range(3):
        for j in range(3):
            print(TT[i][j], end = " ")#end = "" add space insted of the new line
        print()

    
    #player2
    print(player2,"your symbol is O")
    i = int(input("enter row(0 or 1 or 2):- "))
    j = int(input("enter col(0 or 1 or 2):- "))
    TT[i][j] = "O" 
    for i in range(3):
        for j in range(3):
            print(TT[i][j], end = " ")#end = "" add space insted of the new line
        print()
  
    
    if(TT[0][0] == TT[0][1] == TT[0][2] == "X" ):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][0] == TT[0][1] == TT[0][2] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player2,"is winner")
        c = 0
    elif(TT[1][0] == TT[1][1] == TT[1][2] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player2,"is winner")
        c = 0        
    elif(TT[1][0] == TT[1][1] == TT[1][2] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0 
    elif(TT[2][0] == TT[2][1] == TT[2][2] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player2,"is winner")
        c = 0 
    elif(TT[2][0] == TT[2][1] == TT[2][2] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0  
    elif(TT[0][0] == TT[1][1] == TT[2][2] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player2,"is winner")
        c = 0 
    elif(TT[0][0] == TT[1][1] == TT[2][2] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0 
    elif(TT[0][2] == TT[1][1] == TT[2][0] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player2,"is winner")
        c = 0 
    elif(TT[0][2] == TT[1][1] == TT[2][0] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][0] == TT[1][0] == TT[2][0] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][1] == TT[1][1] == TT[2][1] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][2] == TT[1][2] == TT[2][2] == "X"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][0] == TT[1][0] == TT[2][0] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][1] == TT[1][1] == TT[2][1] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0
    elif(TT[0][2] == TT[1][2] == TT[2][2] == "O"):
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        print(player1,"is winner")
        c = 0         
    else:
        for i in range(3):
            for j in range(3):
                print(TT[i][j], end = " ")#end = "" add space insted of the new line
            print()
        c = 1
                
    
 

