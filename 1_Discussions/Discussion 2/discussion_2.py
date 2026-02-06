from turtle import *

### write all new functions here ###
#Nice circle! try making the eyes
#FYI: you only need to have begin_fill and end_fill once. Check this out: https://www.geeksforgeeks.org/python/turtle-begin_fill-function-in-python/

def draw_emoji(turtle):
    """
    Write a function to draw an emoji.
    """
    turtle.pendown()
    turtle.circle(100)
    turtle.fillcolor("yellow")
    turtle.goto(50,50)
    turtle.circle(10)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.circle(10)
    turtle.left(180)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(10)

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """

    space = Screen()
    space.bgcolor("#3A3B3C")
    t = Turtle ()
    draw_emoji(t)
    space.exitonclick()


if __name__ == '__main__':
    main()


