#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:45:33 2021

@author: Shannon Duvall

This file provides the graphics for the game of Pig.
"""
import turtle
import time

# Initializing code.
joe = turtle.Turtle()

# Number of pixels representing the score to win the game.
road_length = 1000
turtle.setup(road_length+50,800)
joe.speed('fastest')
joe.hideturtle()
"""
Dice variables
"""
# Defines the positions of the six pips of a die.
pips = [(20,60),(40,60),(60,60),
        (20,40),(40,40),(60,40),
        (20,20),(40,20),(60,20)]

# Which pips should be drawn to represent each number.
pip_positions = {
    1:[4],
    2:[0,8],
    3:[2,4,6],
    4:[0,2,6,8],
    5:[0,2,4,6,8],
    6:[0,2,3,5,6,8]}
dice_position_1 = (-100,0)
dice_position_2 = (20,0)
dice_size = 80
dice_color = "white"
pip_color = "black"

"""
Turtles and writers for each player
"""
colors = ['red', 'blue']
player1 = turtle.Turtle()
player1.hideturtle()
player2 = turtle.Turtle()
player2.hideturtle()
player1.shape("turtle")
player1.fillcolor(colors[0])
player2.shape("turtle")
player2.fillcolor(colors[1])
player1stamps = []
player2stamps = []
writer1 = player1.clone()
writer1.penup()
writer1.hideturtle()
writer2 = player2.clone()
writer2.penup()
writer2.hideturtle()

"""
The messages turtles write to the screen
"""
messages = turtle.Turtle()
messages.hideturtle()
messages.penup()
messages.goto(-400,40)
messages2 = turtle.Turtle()
messages2.hideturtle()
messages2.penup()
messages2.goto(-400,0)


turtles = [player1,player2]
stamp_collections = [player1stamps, player2stamps]
writers = [writer1,writer2]

"""
  This function should be called when the game starts to 
  initialize the window.
"""
def startup():
    joe.penup()
    joe.goto(road_length//2,300)
    joe.pensize(10)
    joe.pencolor("yellow")
    joe.pendown()
    joe.goto(road_length//2,-200)
    joe.penup()
    joe.goto(-road_length//2,300)
    joe.pencolor("green")
    joe.pendown()
    joe.goto(-road_length//2,-200)
    joe.pensize(1)
    joe.pencolor("black")
    joe.penup()
    player1.penup()
    player1.hideturtle()
    player2.penup()
    player2.hideturtle()
    player1.goto(-road_length//2-10,200)
    writer1.setposition(-road_length//2-10,220)
    writer1.write("Score: 0", False, font=('monaco',20,'bold'))
    player2.goto(-road_length//2-10,-100)
    player1.showturtle()
    player2.showturtle()
    writer2.setposition(-road_length//2-10,-80)
    writer2.write("Score: 0", False, font=('monaco',20,'bold'))

"""
  This function should be called whenever the dice 
  are rolled, so the results of the rolls are drawn.
  Takes two integer inputs which must be between 1 and 6 inclusive.
"""
def roll(d1, d2):
    if d1 < 1 or d2 < 1 or d1 > 6 or d2 > 6:
        print("Input roll values are not between 1 and 6")
    turtle.tracer(False)
    draw(d1,dice_position_1[0], dice_position_1[1])
    draw(d2,dice_position_2[0], dice_position_2[1])
    turtle.tracer(True)
    messages2.clear()
    if d1 == 1 or d2 == 1:   
        messages2.write("Oh no. " + \
                "Roll is: "+str(d1)+" "+str(d2),
                False, font=('monaco',20,'bold'))
        time.sleep(2)
    else:
        messages2.write("You rolled: "+str(d1)+ " and "+str(d2), 
                   False, font=('monaco',20,'bold'))

    
# Helper function for roll.  Draws one die roll at the given position
def draw(roll, x, y):
    joe.penup()
    joe.goto(x,y)
    joe.setheading(0)
    joe.pencolor("black")
    joe.fillcolor(dice_color)
    joe.begin_fill()
    joe.pendown()
    for i in range(4):
        joe.forward(dice_size)
        joe.left(90)
    joe.penup()
    joe.end_fill()
    if roll not in pip_positions:
        print("Oops - random error: ",roll)
    else:
        for index in pip_positions[roll]:
            (pipx,pipy) = pips[index]
            joe.goto(x+pipx, y+pipy)
            joe.dot(10)
    joe.penup()
    joe.hideturtle()

"""
This functions hould be called when the player whose turn
it is changes.  The input is either 1 or 2, telling the 
current player.
"""
def whose_turn(player_number):
    print(player_number)
    if player_number == 1:
        player1.fillcolor(colors[0])
        player2.fillcolor("black")
    else:
        player1.fillcolor("black")
        player2.fillcolor(colors[1])
    messages.clear()
    name = colors[player_number-1].capitalize()
    messages.write(name+"'s Turn.",False, font=('monaco',24,'bold'))    
"""
The race function should be called to update the score of 
a player.  

It takes two inputs - the player number (either 1 or 2), 
and the current score.
"""
def race(player_number, total_score):
    my_turtle = turtles[player_number-1]
    stamps = stamp_collections[player_number-1]
    score_increase = total_score//2 - len(stamps)
    writer = writers[player_number-1]
    for i in range(score_increase):
        stamps.append(my_turtle.stamp())
        my_turtle.forward(road_length//50)
    (xpos,ypos) = my_turtle.pos()
    writer.clear()
    xwriting = min(xpos,road_length//2-200)
    writer.setposition(xwriting,ypos+20)
    writer.write("Score: "+str(total_score), False, font=('monaco',20,'bold'))


"""
The ask function should be called to ask the player if they 
want to roll again or stop.

It takes two inputs - the score for their turn and their total score
for the game.  It returns the text they type in, in lower case.
"""
def ask(round_points, total_score):
    text = "You have "+ str(round_points)+" for this round\n " + \
                   "and "+ str(total_score) + \
                   " overall\n Type r to roll\n and s to stop."
    return turtle.textinput("Turtle Dice Race", text).lower()

"""
The winner function prints a message declaring the winner.

It takes one input - the player number of the winning player.
"""
def winner(number):
    name = colors[number-1].upper()
    messages.clear()
    messages2.clear()
    messages.write(name + " WINS!!",False, font=('monaco',32,'bold'))

"""
The reset function is called when someone rolls snake eyes.
This function erases the turtles showing the score.
It takes as input the player number to reset - either 1 or 2.
"""
def reset(player_number):
    my_turtle = turtles[player_number-1]
    my_turtle.clear()
    stamps = stamp_collections[player_number-1]
    stamps.clear()
    writer = writers[player_number-1]
    my_turtle.setx(-road_length//2-10)
    (xpos,ypos) = my_turtle.pos()
    writer.clear()
    writer.setposition(xpos,ypos+20)
    writer.write("Score: 0", False, font=('monaco',20,'bold'))

"""
This function should always be called at the end of the game
to exit the graphics window cleanly.
"""
def done():
    turtle.done()
    turtle.bye()

