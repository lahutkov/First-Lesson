
percentages = [0.25, 0.20, 0.30, 0.06,]

from turtle import *

radius = 200

penup()
forward(radius)
left(90)
pendown()
color('orange')
begin_fill()
circle(radius)
end_fill()
home()
right(90)
color('black')
def segment(percentages):
    rollingPercent = 0
    radius=200
    for percent in percentages:
        segment = percent * 360
        rollingPercent += segment
        setheading(rollingPercent)
        pendown()
        forward(radius)
        penup()
        home()
segment(percentages)


