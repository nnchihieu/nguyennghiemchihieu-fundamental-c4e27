# #1
from turtle import *
speed(1)
color("red")
right(30)
for i in range(4):
    for j in range(4):
        forward(50)
        if(j%2!=0): left(120)
        else: left(60)
    left(90)

#2
from turtle import *
speed(1)
color("red")
forward(100)
color("blue")
for i in range(2):
    left(120)
    forward(100)
right(150)
color("red")
for j in range(3):
    forward(100)
    right(90)
right(108)
color("blue")
for n in range(4):
    forward(100)
    left(72)
color("red")
for m in range(6):
    forward(100)
    left(60)

mainloop()




