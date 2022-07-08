from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.pendown()
timmy.width(10)

color_list = ["turquoise", "cyan", "teal", "aquamarine", "light sky blue", "deep sky blue", "dodger blue", "cornflower blue", "blue", "medium blue"]
directions = [0, 90, 180, 270]

for i in range(200):
  timmy.color(choice(color_list))
  timmy.forward(30)
  timmy.setheading(choice(directions))


screen = Screen()
screen.exitonclick()
