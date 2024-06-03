import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colores = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + (turtle_index * 40))
    new_turtle.color(colores[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else:
                print(f"you've lose. the {winning_color} turtle is the winner!")

            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
