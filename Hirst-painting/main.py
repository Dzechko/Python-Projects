'''import colorgram

colors = colorgram.extract('image2.jpg', 30)
ls = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    ls.append(new_color)
print(ls)'''  # no need for the code as we got our required color
import random
import turtle

turtle.colormode(255)
color_list = [(211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]

micky = turtle.Turtle()

micky.penup()
micky.hideturtle()
micky.setheading(225)
micky.forward(255)
micky.setheading(0)
micky.speed("fastest")
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    micky.dot(20,random.choice(color_list))
    micky.forward(40)

    if dot_count % 10 == 0:
        micky.setheading(90)
        micky.forward(40)
        micky.setheading(180)
        micky.forward(400)
        micky.setheading(0)


screen = turtle.Screen()
screen.exitonclick()

