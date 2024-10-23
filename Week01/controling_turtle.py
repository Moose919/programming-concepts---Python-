import turtle

window = turtle.Screen()
window.setup(0.5, 0.75)
window.bgcolor(1, 1, 0)
window.title("Activity Program")

dave = turtle.Turtle()
dave.color("#0000FF")
dave.shape("turtle")
dave.goto(0, 0)
dave.turtlesize(4)

# Move to the 3rd quadrant
dave.penup()
dave.right(90)
dave.forward(180)
dave.right(90)  
dave.forward(180)
dave.pendown()

#move up to first qaudrent 
dave.right(90)
dave.forward(400)
dave.right(90)
dave.forward(400)


turtle.done()
