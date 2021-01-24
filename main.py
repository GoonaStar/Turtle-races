from turtle import Turtle, Screen
import random

# Set the attributes of the object
is_game_playable = False
is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]
turtle_list = []

# Validate the input of the user
if user_bet.lower() in colors:
    is_game_playable = True

# Set up the initial pos of the turtle
if is_game_playable:
    for index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(-230, y_pos[index])
        turtle_list.append(new_turtle)
    is_game_on = True

#  Fix the limit and the winner
while is_game_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            winner_turtle = turtle.pencolor()
            if user_bet == winner_turtle:
                print(f"You won! The winner is turtle {winner_turtle}")
            else:
                print(f"The turtle {turtle.pencolor()} win")
            is_game_on = False



screen.listen()
screen.exitonclick()

