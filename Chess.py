#imports the nessisary items from os to clear the screen
from os import system, name
#imports key press
from msvcrt import getch
#possible ACII char
selected = ['#','!','@','$','%','^','&','*','/','\ ','|','-','[',']','{','}','<','>']
selected[9] = selected[9].strip()
colors = ["\033[1;37;40m ","\033[0;37;40m ", "\033[1;36;40m ", "\033[0;36;40m ", "\033[1;35;40m ", "\033[0;35;40m ", "\033[1;34;40m ", "\033[0;34;40m ", "\033[1;32;40m ", "\033[0;32;40m ", "\033[1;31;40m ", "\033[0;31;40m ", "\033[1;33;40m ", "\033[0;33;40m ", "\033[1;30;40m ", "\033[0;30;40m "]
#The function to clear the screen
def sc():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

back = '\033[1;37;40m'

class cursor:
   def __init__(self, xpos, ypos, shape, spos, color, cpos, selector, copie = [], on = True):
      self.xpos = int(xpos)
      self.ypos = int(ypos)
      self.shape = str(shape)
      self.spos = int(spos)
      self.color = str(color)
      self.cpos = int(cpos)
      self.selector = bool(selector)
      self.copie = copie
      self.on = bool(on)

   def keycheck(self):
      key = getch()
      if key != None:
         if key == b'w' and self.ypos != 0:
            self.ypos -= 1
         elif key == b's' and self.ypos < hei - 1:
            self.ypos += 1
         elif key == b'a' and self.xpos != 0:
            self.xpos -= 1
         elif key == b'd' and self.xpos < wid - 1:
            self.xpos += 1
         elif key == b'q':
            if self.selector == True:
               if self.spos == 0:
                  self.spos = len(selected) - 1
               else:
                  self.spos -= 1
               self.shape = selected[self.spos]
            else:
               if self.cpos == 0:
                  self.cpos = len(colors) - 1
               else:
                  self.cpos -= 1
               self.color = colors[self.cpos]
            
         elif key == b'e':
            if self.selector == True:
               if self.spos == len(selected) - 1:
                  self.spos = 0
               else:
                  self.spos += 1
               self.shape = selected[self.spos]
            else:
               if self.cpos == len(colors) - 1:
                  self.cpos = 0
               else:
                  self.cpos += 1
               self.color = colors[self.cpos]

         elif key == b'r':
            if self.selector == True:
               self.selector = False
            else:
               self.selector = True

         elif key == b'z':
            bord[self.ypos][self.xpos] = ''.join(self.color + self.shape + back)

         elif key == b'x':
            if self.on == True:
               self.on = False
            else:
               self.on = True

         elif key == b'c':
            if len(self.copie) < 2:
               self.copie.append(self.ypos)
               self.copie.append(self.xpos)
               bord[self.ypos][self.xpos] = ''.join(' \033[0;31;43m' + 'c' + back)
            else:
               self.copie.append(self.ypos)
               self.copie.append(self.xpos)
               cy = abs(self.copie[0] - self.copie[2])
               cx = abs(self.copie[1] - self.copie[3])
               if self.copie[0] < self.copie[2]:
                  lessy = self.copie[0]
               else:
                  lessy = self.copie[2]

               if self.copie[1] < self.copie[3]:
                  lessx = self.copie[1]
               else:
                  lessx = self.copie[3]

               for i in range (cy + 1):
                  for x in range (cx + 1):
                     bord[i + lessy][x + lessx] = ''.join(self.color + self.shape + back)
               self.copie = []

         elif key == b'h':
            sc()
            print('On Bord:  | Actions:')
            print('   w      |   q - move selected position left by 1')
            print('   |      |   e - move selected position right by 1')
            print('a--@--d   |   r - change currect selected options')
            print('   |      |   z - set current cursor position to selected shape + color')
            print('   s      |   x - toggle cursor view')
            print('          |   c - place 2 point and fill area, select shape after 1st point')
            input('')

C = cursor(0, 0, '#', 0, '\033[1;37;40m ', 0, True)

#Starts program
print('ANSI Printer')
print('press enter to contine')
input('')
sc()


while True:
   try:
      #asks user for height and width
      hei = int(input('What Height of space do you want: '))
      if hei == 0:
         hei += 1
      if hei > 25:
         hei = 25

      break
      
   except:
      print('please enter an intager!')
      input('')
      sc()

while True:
   try:
      wid = int(input('What Wide of space do you want: '))
      if wid == 0:
         wid += 1
      if wid > 35:
         wid = 35
      break

   except:
      print('please enter something reasomble')
      input('')
      sc()

sc()

#creats the bord      
bord = []
for i in range (hei):
   bord.append([' *'] * wid)

#prints the paper
def printpaper():
   #stores the object under the cursor
   storarea = bord[C.ypos][C.xpos]
   if C.on == True:
      #sets position to cursor
      bord[C.ypos][C.xpos] = ' _'
   for i in range (hei):
      print(''.join(bord[i]))
   bord[C.ypos][C.xpos] = storarea
   print('\n')
   if C.selector == True:
      print('>  ' + ' '.join(selected))
      print('   ' + '  ' * C.spos + '\033[1;31;40m^')
      print('\n')
      print('`'.join(colors) + '`')
      print(' ' * ((C.cpos * 2) + 1) + '\033[1;37;40m^')
   else:
      print('\033[1;30;40m' + ' '.join(selected))
      print('  ' * C.spos + '\033[1;37;40m^' + back)
      print('\n')
      print('> ' + '#'.join(colors) + '#')
      print('  ' + ' ' * ((C.cpos * 2) + 1) + '\033[1;31;40m^')
   print(back)


while True:
   sc()
   printpaper()
   C.keycheck()