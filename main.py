from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
colors = ['red', 'orange', 'yellow','green', 'blue', 'purple']
user_bet_check = False 

while not user_bet_check:
  user_bet = screen.textinput(title = "Make your bet", prompt = "Wich turrle will win the race? Enter a color: ")
  if user_bet in colors:
    user_bet_check = True
    
y_positioms = [-70, -40, -10, 20, 50, 80]


all_turtle = []
for turtle_index in range(0 , 6):
  new_turtle = Turtle(shape = 'turtle')
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x = -230, y = y_positioms[turtle_index])
  all_turtle.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtle:
    if turtle.xcor() > 230:
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
      is_race_on = False

    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)
  
  

screen.exitonclick()