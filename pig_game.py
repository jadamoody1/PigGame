#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:46:50 2021

@author: JadaMoody
"""
# Delete this line if you do not want to use graphics yet.
import window
import random

"""
Using the graphical window:
Call the following functions:

window.startup() 
    This function requires no input and gives no output.  It sets up the 
    graphical window, and should be calledonce, at the very beginning of 
    the game.
            
window.whose_turn(player_number)
    This function switches the current player to be the one indicated by the 
    input. Its input should be either 1 or 2, and it gives no output.

window.roll(dice1, dice2)
    This function draws the dice to the screen. The two inputs should be 
    integers between 1 and 6 inclusive.
    There is no return value.
            
window.race(player, score)
    This function causes the turtles to be drawn across the screen to 
    indicate the score and how close the player is to winning. 
    Its input should be two integers: the player number (either 1 or 2) 
    and the score of that player.  It does not return a value.
            
window.reset(player_number)
    This function makes the turtles drawn toward the finish line disappear 
    from the screen. It is used when the player rolls double ones (snake eyes).
    The input is the player to be reset (either 1 or 2).  It does not return a 
	value.
        
window.ask(round_points, total_score)
    This function causes a pop up window to appear, which tells the player 
    their current point values for both the current round and for the game.  
    It asks the player to type 'r' if they want to roll again and 's' if they 
    want to stop. The inputs are the two score values for the current player, 
    and the output is the letter the user types.
        
window.winner(number) 
    This function prints a winning message.  The input is the number 
    (either 1 or 2) of the winning player.  It returns no output.
        
window.done()
    This function should be called when the game is over, to cleanly close 
    the graphics window.  It uses no input or output.
"""

"""
This function plays one turn for one player.
It should let the player roll until they either choose to stop or they roll
a one.

Its input is the score for the player at the beginning of their turn.
If they roll a single one, it should return 0.
If they roll double ones, (snake eyes), it should return -1
Otherwise, it should return the sum of the rolls.
"""


# This function defines the players turn 
def play_turn(player_total_score):
    # Get to random numbers and call the window.roll function to show dice
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    window.roll(dice1, dice2)
    # If one dice contains a one, return 0
    if dice1 == 1 or dice2 == 1:
        return 0
    
    # If both dice roll a one, return -1         
    if dice1 == 1 and dice2 == 1:
        return -1
    
    # Otherwise, add the vaule of the dice to their points this round 
    else:
        round_points = dice1 +dice2
        
    # Ask the player if they want to roll again
    while window.ask(round_points, player_total_score) == 'r':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        window.roll(dice1, dice2)
        if dice1 == 1 or dice2 == 1:
            return 0
            
        elif dice1 == 1 and dice2 == 1:
            return -1
        
        # Returns the points they earned if they didn't roll a one
        else:
            round_points =  round_points + dice1 + dice2
    return round_points

    # If player doesn't want to roll again, return their total score.
    if window.ask(round_points, player_total_score) == 's':
        return player_total_score
            

       
    
            
    

# This function plays the game
def play_game():
    # This function sets up the game window
    window.startup()
    # Players start with 0 points
    player1_total = 0
    player2_total = 0
    while player1_total < 100 and player2_total < 100:
        window.whose_turn(1)  # Defines player 1's turn
        player1 = play_turn(player1_total)
        if player1 == -1:    # If they roll snake eyes
            player1_total = 0
            window.reset(1) # reset the player back to 0
            window.whose_turn(2)  # and it's player 2's turn
        else:
            player1_total = player1_total + player1 #Add the points to total
            window.race(1, player1_total)   # and call the race function
            

        window.whose_turn(2) # Defines player 2's turn
        player2 = play_turn(player2_total)
        if player2 == -1:  # If they roll snake eyes
            player2_total = 0
            window.reset(2) # reset the player back to 0
            window.whose_turn(1) # and its player 1's turn
        else:
            player2_total = player2_total + player2 # Add the points to total
            window.race(2, player2_total)  # and call the race function
    # Determines the winner        
    if player1_total >= 100:
        window.winner(1)
    elif player2_total >= 100:
        window.winner(2)
    window.done()   # Closes the graphical window
   
   
        
        



if __name__ == '__main__':
    play_game()
  
