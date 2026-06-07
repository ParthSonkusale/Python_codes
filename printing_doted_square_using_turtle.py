import turtle
import random

seq = turtle.Turtle()

turtle.bgcolor("black")

width = 5
height = 7

colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "violet",
    "navy",
    "skyblue",
    "lime",
    "maroon",
    "teal"
]

seq.penup()
seq.setpos(-300,300)

def spiral(m,n):
    k = 0
    l = 0
    f = 0
    
    
    col = random.randint(0 ,21)
    seq.pencolor(colors[col])
                 
    while(k < m and l < n):    
        
        
        if(f == 1):
            seq.right(90)
            
        # first row
        for i in range(l , n):
            seq.dot()
            seq.forward(30)
        
        k = k + 1
        f = 1
        
        seq.right(90)
        col = random.randint(0 ,21)
        seq.pencolor(colors[col])
        # last column
        for i in range(k , m):
            seq.dot()
            seq.forward(30)
        
        n = n - 1
        
        seq.right(90)
        
        if(k < m):
            col = random.randint(0 ,21)
            seq.pencolor(colors[col])
            # last row
            for i in range(n - 1 , l - 1 , -1):
                seq.dot()
                seq.forward(30)
        
            m = m - 1
        
        seq.right(90)
        
        # first column
        if(l < n):
            col = random.randint(0 ,21)
            seq.pencolor(colors[col])
            for i in range(m - 1 , k - 1 , -1):
                seq.dot()
                seq.forward(30)
        
            l = l + 1

spiral(20,20)

turtle.done()