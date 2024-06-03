from turtle import Turtle


# Create a Paddle class

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.cor = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
















# # Create a Paddle object
# paddle = Turtle(shape="square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(y=0, x=350)
#
#
# # Create movement of paddles
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), y=new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), y=new_y)
