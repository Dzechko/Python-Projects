from turtle import Turtle, Screen
from paddle import Paddle

# Create a Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong-game")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

# make the screen listens to keyboard strokes

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
