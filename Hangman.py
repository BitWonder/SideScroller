import os
import time as t

#function to clear the screen of current text
def clear():
   os.system('cls' if os.name == 'nt' else "printf '\033c'")

#the chosser class dose all the heavy lifting and prints the text along with being the class that chosses the word
class chosser():
   def __init__(self,keys=[], word = ['h', 'a', 'n', 'g', 'm', 'a', 'n'], player = 2, score = [0, 0], death = 0, correctguesses = [''],phrase='Word'):
      self.word = word #the word/phrase to guess
      self.player = player #player 1 or 2
      self.score = score #score of each so when one gets to 3 it stops
      self.death = death #how many failed attempts a player has
      self.correctguesses = correctguesses #the list of letters the player has correctly guessed
      self.keys = keys #the keys the player pressed
      self.phrase = phrase

   #gives the next player a chance to make a word
   def changeWord(self):
      clear()
      print("Player",self.player)
      w = input("what's the new word/phrase: ")
      w = w.lower()
      self.phrase = 'Word'
      self.death = 0
      self.word = list(w)
      self.correctguesses = [' ']
      self.correctguesses.clear()
      self.keys.clear()
      for x in range (len(self.word)):
         if self.word[x] == ' ':
            self.correctguesses.append(' ')
            self.phrase = 'phrase'
         elif self.word[x] == "'":
            self.correctguesses.append("'")
         elif self.word[x] == "-":
            self.correctguesses.append('-')
         else:   
            self.correctguesses.append('#')
   
   #checks the word
   def hangman(self, guess):
      check = False
      for x in range (len(self.word)):
         if guess == self.word[x]:
            self.correctguesses[x] = self.word[x]
            check = True
      if check == False:
         self.death += 1

   #prints the guessed letters the hangman and amount of letters needed
   def printman(self):
      p = []
      for x in range (len(self.correctguesses)):
         if self.correctguesses[x] != self.word[x]:
            p.append('#')
         else:
            p.append(self.word[x])
      clear()
      if self.death == 0:
         print(' '.join(p))
      elif self.death == 1 or self.death == 2:
         print(' '.join(p), '@')
      elif self.death > 2:
         print(' '.join(p), ' @')
      p = []
      p = '_' * len(self.correctguesses)
      if self.death < 2:
         print(' '.join(p))
      elif self.death == 2:
         print(' '.join(p), '|')
      elif self.death == 3:
         print(' '.join(p), '-|')
      elif self.death > 3:
         print(' '.join(p), '-|-')
      if self.death < 5:
         print(' '.join(p))
      if self.death == 5:
         print(' '.join(p), '/')
      elif self.death >= 6:
         print(' '.join(p), '/ \ ')
      print('\n')
      print('Score:',a.score[1],'-',a.score[0])
      print("Key's used: " + '-'.join(a.keys))

#asks the player for the guess and sends it of to chosser            
class guesser():
   def __init__(self):
      pass
      
   def guess(self):
      if a.player == 2:
         l = list(input("Player 1 what's your guess: ").lower())
      else:
         l = list(input("Player 2 what's your guess: ").lower())
      try:
         l = l[0]
         a.keys.append(l)
         a.hangman(l)
      except:
         pass

#I WAS IN A HURRY
a = chosser()
b = guesser()

#the while loop to run the thing
while a.score[0] < 3 and a.score[1] < 3:
   a.changeWord()
   prev = a.score
   while a.score == prev:
      a.printman()
      b.guess()
      if a.death >= 6:
         a.printman()
         t.sleep(1)
         print('You lose')
         print("The",a.phrase,"was:",''.join(a.word))
         t.sleep(3)
         a.score[a.player - 1] -= 1 
         if a.player == 2:
            a.player = int(1)
         else:
            a.player = int(2)
         break
      worng = False
      for x in range(len(a.correctguesses)):
         if a.correctguesses[x] == a.word[x]:
            pass
         else:
            worng = True
      if worng == False:
         clear()
         a.printman()
         print('You beat the',a.phrase+'!')
         t.sleep(3)
         a.score[a.player-1] += 1
         if a.player == 2:
            a.player = 1
         else:
            a.player = 2
         break

#prints which player has won the game
clear()
print('The score is',a.score[1],'-',a.score[0],'and...')
if a.score[0] == 3:
   print("Player 2 wins!")
else:
   print("Player 1 wins!")