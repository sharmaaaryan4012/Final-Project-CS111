"""
Final Project
Course: CS 111
Prof:   Shanon Reckinger
Year:   2022-23
Names:  Aaryan Sharma, Ayush Bhardwaj
"""

import turtle
import random
import image

def square(sq, x, y, color):
  sq.fillcolor(color)
  sq.pencolor(color)
  sq.turtlesize("5")
  sq.goto(x,y)
  sq.stamp

def board():
  print("hello")



s = turtle.getscreen()
s.bgcolor("black")
board()

turtle.mainloop() # uncomment once you start doing turtle drawing