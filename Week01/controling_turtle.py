#import 's the turtle screen 
import turtle
window = turtle.Screen() 
window.setup(0.5, 0.75) 
window.bgcolor(1, 1, 0) 
#Title of the output window
window.title("Activity Program")
#create turtle 
dave = turtle.Turtle() #Pointer/pen
dave.color(0, 10, 0) #Pointer/pen color
dave.shape("turtle") #Pointer/pen shape
dave.goto(0,0) #Pointer movement
turtle.done() #Render the screen
