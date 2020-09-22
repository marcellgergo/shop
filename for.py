
import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
n=360
h=1
sz=360/n
for i in range (n):
    alex.forward (h)
    alex.left (sz) 
