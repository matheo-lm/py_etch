from turtle import Turtle, Screen

tim = Turtle()
screen =  Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_up():
    tim.left(10)

def move_down():
    tim.right(10)

def move_clears():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="c", fun=move_clears)

screen.exitonclick()
