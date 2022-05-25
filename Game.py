#allows us to clear screen
from os import system, name
#use rand for sudo random number
import random as rand
#to move around
from getch import getch

def SC():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def flat(floor, direction):
   if direction == False:
      for i in range (hei):
         D2ZONE[i].pop()
         if i < floor:
            x = rand.randint(1, 75)
            if x != 1:
               D2ZONE[i].insert(0, '*')
            elif x == 1:
               D2ZONE[i].insert(0, '-')
         elif i == floor:
            D2ZONE[i].insert(0, '_')
         else:
            x = rand.randint(1, 75)
            if x != 1:
               D2ZONE[i].insert(0, '#')
            elif x == 1:
               D2ZONE[i].insert(0, '%')
   else:
      for i in range (hei):
         D2ZONE[i].pop(0)
         if i < floor:
            x = rand.randint(1, 75)
            if x != 1:
               D2ZONE[i].append('*')
            elif x == 1:
               D2ZONE[i].append('-')
         elif i == floor:
            D2ZONE[i].append('_')
         else:
            x = rand.randint(1, 75)
            if x != 1:
               D2ZONE[i].append('#')
            elif x == 1:
               D2ZONE[i].append('%')

def layprint():
   for i in range (hei):
      print(''.join(D2ZONE[i]))

def noise(start, direction):
   start = int(start)
   direction = bool(direction)
   way = rand.randint(1,5)
   #going down so start go up
   if way == 1:
      if start + 1 < hei - 1 and start + 2 < hei - 1:
         start += 1
         if direction == False:
            for i in range (hei):
               D2ZONE[i].pop()
               if i < start:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].insert(0, '*')
                  elif x == 1:
                     D2ZONE[i].insert(0, '-')
               elif i == start:
                  D2ZONE[i].insert(0, '/')
               else:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].insert(0, '#')
                  elif x == 1:
                     D2ZONE[i].insert(0, '%')
         elif direction == True:
            for i in range (hei):
               D2ZONE[i].pop(0)
               if i < start:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].append('*')
                  elif x == 1:
                     D2ZONE[i].append('-')
               elif i == start:
                  D2ZONE[i].append('\ '.strip())
               else:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].append('#')
                  elif x == 1:
                     D2ZONE[i].append('%')
         return 1
      else:
         flat(start, direction)
         return 0

   elif way == 3:
      #floor goes up so start go down
      if start - 1 > 0 and start - 2 > 0:
         if direction == False:
            for i in range (hei):
               D2ZONE[i].pop()
               if i < start:
                  D2ZONE[i].insert(0, '*')
               elif i == start:
                  D2ZONE[i].insert(0, '\ '.strip())
               else:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].insert(0, '#')
                  elif x == 1:
                     D2ZONE[i].insert(0, '%')
         elif direction == True:
            for i in range (hei):
               D2ZONE[i].pop(0)
               if i < start:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].append('*')
                  elif x == 1:
                     D2ZONE[i].append('-')
               elif i == start:
                  D2ZONE[i].append('/')
               else:
                  x = rand.randint(1, 75)
                  if x != 1:
                     D2ZONE[i].append('#')
                  elif x == 1:
                     D2ZONE[i].append('%')
         start -= 1
         return -1
      else:
         flat(start, direction)
         return 0

   #floor stays the same
   else:
      flat(start, direction)
      return 0

wid = 50
hei = 15

#set the original layout
D2ZONE = []
for i in range (hei):
   D2ZONE.append(['*'] * wid)


SC()

layprint()

SC()

x = int(13)
for i in range (wid):
   x = x + noise(x, False)

layprint()

save = None
saveint = None
jump = False
while True:
   key = getch()
   if key != None:
      if key == 'a':
         for i in range (hei):
            if D2ZONE[i][0] == '_':
               noise(i, False)
               break
            elif D2ZONE[i][0] == '/':
               noise(i, False)
               break
            elif D2ZONE[i][0] == '\ '.strip():
               noise(i - 1, False)
               break
      elif key == 'd':
         for i in range (hei):
            if D2ZONE[i][wid - 1] == '_':
               noise(i, True)
               break
            elif D2ZONE[i][wid - 1] == '\ '.strip():
               noise(i, True)
               break
            elif D2ZONE[i][wid - 1] == '/':
               noise(i - 1, True)
               break
      elif key == ' ':
         jump = True
      for i in range (hei):
         if D2ZONE[i][25] == '_' or D2ZONE[i][25] == '/' or D2ZONE[i][25] == '@' or D2ZONE[i][25] == '\ '.strip():
            if jump == False:
               save = D2ZONE[i][25]
               saveint = i
            else:
               save = D2ZONE[i - 1][25]
               saveint = i - 1
            if jump == False:
               D2ZONE[i][25] = '@'
            else:
               D2ZONE[i-1][25] = '@'
               jump = False
      SC()
      layprint()
      D2ZONE[saveint][25] = save