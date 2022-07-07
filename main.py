from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
timmy.pendown()
timmy.width(10)

color_list = ["turquoise", "cyan", "teal", "aquamarine", "light sky blue", "deep sky blue", "dodger blue", "cornflower blue", "blue", "medium blue"]

for i in range(100):
  timmy.color(choice(color_list))
  num = randint(1, 4)
  if num == 1:
    timmy.backward(50)
  elif num == 2:
    timmy.forward(50)
  elif num == 3:
    timmy.left(90)
    timmy.forward(50)
  else:
    timmy.right(90)
    timmy.forward(50)
      
screen = Screen()
screen.exitonclick()