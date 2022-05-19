import os
import random as r
import time as t
YList = ['y','ya','yes','life','okay','ok','ye']
RPSList = ['Rock', 'Paper', 'Sicors']
GraphicsRPSList = ['[]','__','OO\n/\ ']
def clear(): #The clear function
   os.system('cls' if os.name == 'nt' else "printf '\033c'")

#doy you want to play the game
def play(a):
   if a == False:
      p = str(input("Do you want to play, Rock-Paper-Sicors: ")).lower()
   else:
      p = str(input("Do you want to play again: "))
   if p in YList:
      return True
   else:
      return False
   
#chosse a rock, some paper, or a pair of sicors
def chosse(place = 0):
   while True:
      clear()
      print('Chosse:')
      for x in range (len(RPSList)):
         if x == place:
            print(RPSList[x],'<')
         else:
            print(RPSList[x])
      print('\n')
      way = str(input('UP: w\nDown: s\nEnter: e\n').lower())
      if way == 'w':
         if place != 0:
            place -= 1
      elif way == 's':
         if place != len(RPSList)-1:
            place += 1
      else:
         return place

#finds who win the game
def find(ch, bot):
   if ch == 0:
      if bot == 1:
         win = 2
      elif bot == 2:
         win = 1
      else:
         win = 0
   elif ch == 1:
      if bot == 2:
         win = 2
      elif bot == 0:
         win = 1
      else:
         win = 0
   else:
      if bot == 0:
         win = 2
      elif bot == 1:
         win = 1
      else:
         win = 0
   return win
   
a = False
game = play(a)
a = True
#game loop
while game == True:
   ch = chosse()
   bot = r.randrange(0,3)
   win = find(ch, bot)
   if win == 1:
      print(GraphicsRPSList[ch]+ '\n\n\bBeats\n\n'+ GraphicsRPSList[bot]+ '\n \n \bYou win!')
      t.sleep(3)
   elif win == 2:
      print(GraphicsRPSList[bot]+ '\n\n\bBeats\n\n'+ GraphicsRPSList[ch]+ '\n \n \bYou Lose')
   else:
      print('Tie')
      t.sleep(3)
   if win == 0:
      pass
   elif win != 0:
      game = play(a)