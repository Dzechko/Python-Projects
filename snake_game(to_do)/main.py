from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# create snake body.
segments = []

for turtle_index in range(0,3):
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(x=(-turtle_index*20),y=0)
    segments.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(start=2,stop=-1,step=1):
        pass










screen.exitonclick()