import msvcrt
import random
import os
import time

def car_game():
   speed = 10
   cord = 4
   def screen_clear():
      if os.name == 'posix':
         _ = os.system('clear')

      else:
         _ = os.system('cls')

   def moveca(a, speed, cord):
      if a == b'a':
         cord = cord - 1
      if a == b'd':
         cord = cord + 1
      if a == b's':
         speed = speed + 1
      if a == b'w':
         speed = speed - 1
      time.sleep(speed * 0.1)

   yes_list = ['y', 'ye', 'yes', 'ya', 'es', 'yo']    
   score = 0
   endict1 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict2 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict3 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict4 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict5 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict6 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict7 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   endict8 = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   end = {1: '  ', 2: '  ', 3: '  ', 4: '  ', 5: '  ', 6: '  ', 7: '  '}
   carlist = ['  ', '()', '{}', '[]', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

   print('Please enter for car:', '() - 1, {} - 2, [] - 3')
   a = input()
   if a == '1':
      car = '()'
   elif a == '2':
      car = '{}'
   elif a == '3':
      car = '[]'
   else:
      car = 'CR'

   miles = 0

   screen_clear()
   print('Your Car is', car)
   time.sleep(0.1)
   N = input('Do you want to name your car: ')
   N = N.lower()

   if N in yes_list:
      N = input('What name will you give your car: ')
      time.sleep(0.5)
      print(N, car)

   else:
      N = 'Your car'


   screen_clear()
   print('Defult - 1')
   time.sleep(0.8)
   print('Red - 2')
   time.sleep(0.7)
   print('Dark Green - 3')
   time.sleep(0.6)
   print('Light Green - 4')
   time.sleep(0.5)
   print('Yellow - 5')
   time.sleep(0.4)
   print('Blue - 6')
   time.sleep(0.3)
   print('Pink - 7')
   time.sleep(0.2)
   print('Gray - 8')
   time.sleep(0.1)
   cotc = input('Chosse the color of your car: ')
   if cotc == '1':
      cotc = '0'
      cotcs = 'White'
   elif cotc == '2':
      cotc = '31'
      cotcs = 'Red'
   elif cotc == '3':
      cotc = '32'
      cotcs = 'Dark Green'
   elif cotc == '4':
      cotc = '92'
      cotcs = 'Light Green'
   elif cotc == '5':
      cotc = '33'
      cotcs = 'Yellow'
   elif cotc == '6':
      cotc = '34'
      cotcs = 'Blue'
   elif cotc == '7':
      cotc = '95'
      cotcs = 'Pink'
   else:
      cotc = '90'
      cotcs = 'Gray'

   sfs = '\033[' + cotc + 'm'
   sff = '\033[0m'

   screen_clear()
   if car == '()':
      print('Type: Modern')
      time.sleep(0.5)
      print('Color:', cotcs)
      time.sleep(0.5)
      print(N, '-', sfs + car + sff)
      time.sleep(3)

   if car == '{}':
      print('Type: Millitary')
      time.sleep(0.5)
      print('Color:', cotcs)
      time.sleep(0.5)
      print(N, '-', sfs + car + sff)
      time.sleep(3)

   if car == '[]':
      print("Type: 1950's Box")
      time.sleep(0.5)
      print('Color:', cotcs)
      time.sleep(0.5)
      print(N, '-', sfs + car + sff)
      time.sleep(2.5)


   print('w - incresses speed: \n')
   time.sleep(0.5)
   print('        ^^')
   print('        ()')
   time.sleep(1)
   screen_clear()

   print('s - decresses speed: \n')
   time.sleep(0.5)
   print('         ()')
   print('         \/')
   time.sleep(1)
   screen_clear()

   print('a - d moves the car along the lane: \n')
   time.sleep(0.5)
   print('     <-()->')
   time.sleep(1)
   screen_clear()

   print('Press e to cruse and move left if theirs a car infront of you')
   time.sleep(0.5)
   print('        <^')
   print('        ()')
   time.sleep(1)

   print('Press r to cruse and move right if theirs a car infront of you')
   time.sleep(0.5)
   print('        ^>')
   print('        ()')
   time.sleep(1)

   print('Press t to end cruse control')
   time.sleep(0.5)
   print('       !<^!')
   print('        ()')
   time.sleep(1)
   screen_clear()
   print('n to engage nitro!')
   time.sleep(0.5)
   print('        ()')
   print('        ||')
   time.sleep(1)


   screen_clear()

   upcar = 50

   fuel = 100

   nitro = 3

   nitrot = 0

   speedst = 10

   cruise = 'Off'

   while True:
      #input to move car
      if nitrot > 0:
         speed = 0
         nitrot -= 1
         score += 3 * (10 - speed)
      elif nitrot == 0:
         speed = speedst

      if cruise == 'Off' and a != b'w' or a != b's' or a != b'a' or a != b'd':
         grm = random.randrange(0, 4092)
         if grm == 69:
            grm = random.randrange(0, 128)
            if grm == 128:
               if cord == 7:
                  print('Sorry, You Were Unfoucased')
                  exit()
               else:
                  cord += 1
            elif grm == 1:
               if cord == 1:
                  print('Sorry, You Were Unfoucased')
                  exit()
               else:
                  cord -= 1
         
      if msvcrt.kbhit() and nitrot == 0:
         a = msvcrt.getch()
         a = a.lower()
         if a == b'a' and cord != 1:
            cord -= 1
         elif a == b'd' and cord != 7:
            cord = cord + 1
         elif a == b's' and speed != 10 and speed != 10.5 and speed != 9.5:
            speed += 1
            speedst = speed
         elif a == b'w' and speed != 0:
            speed = speed - 0.5
            speedst = speed
         elif a == b'n' and nitro != 0:
            nitro -= 1
            speedst = speed
            speed = 0
            nitrot = 5
         elif a == b'e':
            cruise = 'Set'
            tcm = 'l'
            speed = 10
         elif a == b'r':
            cruise = 'Set'
            tcm = 'r'
            speed = 10
         elif a == b't':
            cruise = 'Off'
            
      if cruise == 'Set':
         speed = 10
         speedst = 10
         if cord == 1:
            if endict8.get(1) != '  ':
                  cord = cord + 1
                     
         if cord == 2:
            if endict8.get(2) != '  ':
               if tcm == 'l':
                  a = b'a'
                  cord -= 1
               else:
                  a = b'd'
                  cord = cord + 1
                     
         if cord == 3:
            if endict8.get(3) != '  ':
               if tcm == 'l':
                  a = b'a'
                  cord -= 1
               else:
                  a = b'd'
                  cord = cord + 1
                     
         if cord == 4:
            if endict8.get(4) != '  ':
               if tcm == 'l':
                  a = b'a'
                  cord -= 1
               else:
                  a = b'd'
                  cord = cord + 1

         if cord == 5:
            if endict8.get(5) != '  ':
               if tcm == 'l':
                  a = b'a'
                  cord -= 1
               else:
                  a = b'd'
                  cord = cord + 1

         if cord == 6:
            if endict8.get(6) != '  ':
               if tcm == 'l':
                  a = b'a'
                  cord -= 1
               else:
                   a = b'd'
                   cord = cord + 1

         if cord == 7:
            if endict8.get(7) != '  ':
                  cord -= 1
                  
      
      score = score + 1
      if score == upcar:
         carlist.remove('  ')
         upcar = upcar + 50 + (upcar // 2)
      time.sleep(speed * 0.1)
      speedre = 10 - speed
      if speed == 0:
         speedre = 'MAX'

      press = 'Press - N'

      fuel = fuel - (0.01 * (10 - speed))

      fuelpre = (fuel // 1)

      miles += 0.1
      
      if fuelpre >= 91:
         tank = '<><><><><><><><><><>'
      elif fuelpre >= 81 and fuelpre <= 90:
         tank = '<><><><><><><><><>'
      elif fuelpre >= 71 and fuelpre <= 80:
         tank = '<><><><><><><><>'
      elif fuelpre >= 61 and fuelpre <= 70:
         tank = '<><><><><><><>'
      elif fuelpre >= 51 and fuelpre <= 60:
         tank = '<><><><><><>'
      elif fuelpre >= 41 and fuelpre <= 50:
         tank = '<><><><><>'
      elif fuelpre >= 31 and fuelpre <= 40:
         tank = '<><><><>'
      elif fuelpre >= 21 and fuelpre <= 30:
         tank = '<><><>'
      elif fuelpre >= 11 and fuelpre <= 20:
         tank = '<><>'
      elif fuelpre >= 1 and fuelpre <= 10:
         tank = '<>'
      else:
         tank = '<'

      screen_clear()
      print('Your score is:', score,"- Speed =", speedre)
      print('|' + endict1.get(1) +'|' + endict1.get(2) +'|' + endict1.get(3) +'|' + endict1.get(4) +'|' + endict1.get(5) +'|' + endict1.get(6)+ '|' + endict1.get(7) + '|', 'fuel:')
      print('|' + endict2.get(1) +'|' + endict2.get(2) +'|' + endict2.get(3) +'|' + endict2.get(4) +'|' + endict2.get(5) +'|' + endict2.get(6) +'|' + endict2.get(7) + '|', str(fuelpre))
      print('|' + endict3.get(1) +'|' + endict3.get(2) +'|' + endict3.get(3) +'|' + endict3.get(4) +'|' + endict3.get(5) +'|' + endict3.get(6) +'|' + endict3.get(7) + '|' + sfs + tank + sff)
      print('|' + endict4.get(1) +'|' + endict4.get(2) +'|' + endict4.get(3) +'|' + endict4.get(4)+ '|' + endict4.get(5) +'|' + endict4.get(6) +'|' + endict4.get(7) + '|', nitro, press)
      print('|' + endict5.get(1) +'|' + endict5.get(2) +'|' + endict5.get(3) +'|' + endict5.get(4)+ '|' + endict5.get(5) +'|' + endict5.get(6) +'|' + endict5.get(7) + '|', 'Miles:', miles)
      print('|' + endict6.get(1) +'|' + endict6.get(2) +'|' + endict6.get(3) +'|' + endict6.get(4)+ '|' + endict6.get(5) +'|' + endict6.get(6) +'|' + endict6.get(7) + '|', '[Cruise] -', cruise)
      print('|' + endict7.get(1) +'|' + endict7.get(2) +'|' + endict7.get(3) +'|' + endict7.get(4) +'|' + endict7.get(5) +'|' + endict7.get(6) +'|' + endict7.get(7) + '|')
      print('|' + endict8.get(1) +'|' + endict8.get(2) +'|' + endict8.get(3) +'|' + endict8.get(4)+ '|' + endict8.get(5) +'|' + endict8.get(6)+ '|' + endict8.get(7) + '|')    
      if cord == 1:
         if end.get(1) != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + sfs + car + sff + '|' + end.get(2) + '|' + end.get(3) + '|' + end.get(4)+ '|' + end.get(5) + '|' + end.get(6) + '|' + end.get(7) + '|')
      if cord == 2:
         if end.get(2) != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + sfs + car + sff + '|' + end.get(3) + '|' + end.get(4)+ '|' + end.get(5) + '|' + end.get(6) + '|' + end.get(7) + '|')

      if cord == 3:
         if end.get(3) != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + end.get(2) + '|' + sfs + car + sff + '|' + end.get(4)+ '|' + end.get(5) + '|' + end.get(6) + '|' + end.get(7) + '|')

      if cord == 4:
         if end.get(4) != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + end.get(2) + '|' + end.get(3) + '|' + sfs + car + sff + '|' + end.get(5) + '|' + end.get(6) + '|' + end.get(7) + '|')

      if cord == 5:
         if end.get(5)  != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + end.get(2) + '|' + end.get(3) + '|' + end.get(4)+ '|' + sfs + car + sff + '|' + end.get(6) + '|' + end.get(7) + '|')

      if cord == 6:
         if end.get(6) != '  ' or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + end.get(2) + '|' + end.get(3) + '|' + end.get(4)+ '|' + end.get(5) + '|' + sfs + car + sff + '|' + end.get(7) + '|')

      if cord == 7:
         if end.get(7) != '  '  or fuel <= 0:
            print('Your score was:', score, '-', N, '-', sfs + car + sff)
            time.sleep(5)
            p = input('Do You Want To Play Again(y/n) ')
            p = p.lower()
            if p == 'y':
               car_game()
            else:
               exit()
         else:
            game = True
            print('|' + end.get(1) + '|' + end.get(2) + '|' + end.get(3) + '|' + end.get(4)+ '|' + end.get(5) + '|' + end.get(6) + '|' + sfs + car + sff + '|')

      end[1] = endict8.get(1)
      endict8[1] = endict7.get(1)
      endict7[1] = endict6.get(1)
      endict6[1] = endict5.get(1)
      endict5[1] = endict4.get(1)
      endict4[1] = endict3.get(1)
      endict3[1] = endict2.get(1)
      endict2[1] = endict1.get(1)
      endict1[1] = random.choice(carlist)

      end[2] = endict8.get(2)
      endict8[2] = endict7.get(2)
      endict7[2] = endict6.get(2)
      endict6[2] = endict5.get(2)
      endict5[2] = endict4.get(2)
      endict4[2] = endict3.get(2)
      endict3[2] = endict2.get(2)
      endict2[2] = endict1.get(2)
      endict1[2] = random.choice(carlist)
      
      end[3] = endict8.get(3)
      endict8[3] = endict7.get(3)
      endict7[3] = endict6.get(3)
      endict6[3] = endict5.get(3)
      endict5[3] = endict4.get(3)
      endict4[3] = endict3.get(3)
      endict3[3] = endict2.get(3)
      endict2[3] = endict1.get(3)
      endict1[3] = random.choice(carlist)

      end[4] = endict8.get(4)
      endict8[4] = endict7.get(4)
      endict7[4] = endict6.get(4)
      endict6[4] = endict5.get(4)
      endict5[4] = endict4.get(4)
      endict4[4] = endict3.get(4)
      endict3[4] = endict2.get(4)
      endict2[4] = endict1.get(4)
      endict1[4] = random.choice(carlist)

      end[5] = endict8.get(5)
      endict8[5] = endict7.get(5)
      endict7[5] = endict6.get(5)
      endict6[5] = endict5.get(5)
      endict5[5] = endict4.get(5)
      endict4[5] = endict3.get(5)
      endict3[5] = endict2.get(5)
      endict2[5] = endict1.get(5)
      endict1[5] = random.choice(carlist)

      end[6] = endict8.get(6)
      endict8[6] = endict7.get(6)
      endict7[6] = endict6.get(6)
      endict6[6] = endict5.get(6)
      endict5[6] = endict4.get(6)
      endict4[6] = endict3.get(6)
      endict3[6] = endict2.get(6)
      endict2[6] = endict1.get(6)
      endict1[6] = random.choice(carlist)

      end[7] = endict8.get(7)
      endict8[7] = endict7.get(7)
      endict7[7] = endict6.get(7)
      endict6[7] = endict5.get(7)
      endict5[7] = endict4.get(7)
      endict4[7] = endict3.get(7)
      endict3[7] = endict2.get(7)
      endict2[7] = endict1.get(7)
      endict1[7] = random.choice(carlist)
      

car_game()
