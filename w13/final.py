from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Turtle Race", "Place your bet:")
COLOR_NAMES = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]
turtles = []
screen.listen()


def go():
    turtles[5].fd(8)


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(COLOR_NAMES[turtle_index])
    new_turtle.setpos(-230, Y_POSITIONS[turtle_index])
    turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    screen.onkey(key='space', fun=go)

    for turtle_num in range(0, 6):
        if turtles[turtle_num].xcor() > 230:
            winner = turtles[turtle_num].pencolor()
            is_race_on = False
            if winner == bet:
                print(f"You won, {winner} finished first!")
            else:
                print(f"You've lost, {winner} finished first.")

    for turtle_num in range(0, 5):

        turtles[turtle_num].fd(randint(0, 10))

screen.exitonclick()
