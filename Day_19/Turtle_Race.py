import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
if user_bet not in colors:
    colors.append(user_bet)
l = len(colors)
for i in range(l):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, (-100 + i * 50))
    all_turtle.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        rabdom_distance = random.randint(0,10)
        turtle.forward(rabdom_distance)
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win...")
            else:
                print("Opps...You Lose!!!")
            race_is_on = False
            break
screen.exitonclick()

