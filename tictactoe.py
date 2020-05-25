#!/usr/bin/env python3

import sys

def instructions():
   print('Welcome to TicTacToe, the age old classic. The goal of the game is to get three in a row,')
   print('first choose X or O then choose who goes first.')
   print('Now, begin playing the game, make a move from 1-9 in the grid, like so:')
   print('\n'.join([
         " _____________________________ ",
         "|         |         |         |",
         "|    1    |    2    |    3    |",
         "|_________|_________|_________|",
         "|         |         |         |",
         "|    4    |    5    |    6    |",
         "|_________|_________|_________|",
         "|         |         |         |",
         "|    7    |    8    |    9    |",
         "|_________|_________|_________|"]))

def start():
   '''Initiates the game by deciding who is X or O, who goes first and gives instructions if 
   neccesary'''
   print('Do you know how to play the game "yes" or "no"')
   a = input()
   if a == 'no':
      instructions()

   print('Choose X or O below')
   player1 = input()
   if player1 in ("X", 'x'):
      player1 = "X"
      player2 = "O"
   else:
      player1 = "O"
      player2 = "X"

   grid = [
         "                 _____________________________ ",
         "  _______       |         |         |         |",
         " |Player1|      |         |         |         |",
         " |   {:s}   |      |_________|_________|_________|".format(player1),
         " |_______|      |         |         |         |",
         "  _______       |         |         |         |",
         " |Player2|      |_________|_________|_________|",
         " |   {:s}   |      |         |         |         |".format(player2),
         " |_______|      |         |         |         |",
         "                |_________|_________|_________|"]

   print("           WELCOME TO TICTACTOE!")
   print('\n'.join(grid))

   print('Who goes first? "p1" or "p2"?')
   player = input()
   if player == 'p1':
      return player1, player1, player2, grid
   else:
      return player2, player1, player2, grid

def winner(p1moves, p2moves):
   '''Determines whether there is a winner or not yet'''
   winning_set = [{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}, 
                  {'1', '4', '7'}, {'2', '5', '8'}, {'3', '6', '9'},
                  {'1', '5', '9'}, {'3', '5', '7'}]
   for s in winning_set:
      if s.issubset(p1moves):
         print('Congratulations Player 1! You are the winner.')
         print('Player 2, you suck never play this game again!')
         return True
      elif s.issubset(p2moves):
         print('Congratulations Player 2! You are the winner.')
         print('Player 1, you suck never play this game again!')
         return True

   return False

def move(turn, pos, grid, mapping):
   '''Executes a move for a player'''
   i, j = mapping[pos]
   grid[i] = grid[i][:j] + turn + grid[i][j + 1:]
   mapping.pop(pos)
   print(mapping)
   return grid

def main():

   turn, player1, player2, grid = start()
   p1moves = set()
   p2moves = set()

   mapping = {
      '1': (2, 21), '2': (2, 31), '3': (2, 41),
      '4': (5, 21), '5': (5, 31), '6': (5, 41),
      '7': (8, 21), '8': (8, 31), '9': (8, 41)
   }

   print('Make your move {:s}'.format(turn))
   i = 0
   while not winner(p1moves, p2moves) and i < 9:
      pos = input()

      while pos not in mapping:         
         print('That spot is taken! Choose a different one!')
         pos = input()

      grid = move(turn, pos, grid, mapping)
      print('\n'.join(grid))

      if turn == player1:
         p1moves.add(pos)
         turn = player2
      else:
         p2moves.add(pos)
         turn = player1
      i += 1
   if len(mapping) == 0:
      print("Oh my, it's a draw! Wow you two are equally matched!")



if __name__ == '__main__':
   main()