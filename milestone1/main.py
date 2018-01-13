'''
Main Executor of the Tic Tac Toe program
'''

import core.gamelogic
from core.gamelogic import GameLogic

choice = None

print 'Welcome to my Dodgey Tic tac Toe game \n'
print 'Please make a selection from the following list:'

print '1. New Game'
print '2. Exit'

choice = raw_input('Please enter your choice: ')

if choice == '1':
    x = GameLogic()
    x.start_game()


