import random
import os

print('Letter Sat - 1')
print('Cyrcle sat - 2')
print('Randoom sat - 3')
sat_choice = input('')
sat_choice = sat_choice.lower()
tat = True
def clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

if sat_choice == 'letter' or sat_choice == 'letter sat' or sat_choice == '1':
    times = input('how many ~seconds do you want this program to last: ')
    times = int(times)
    times = times * 6.8
    times = times // 1
    prinline = [1]
    letter_list = ['`','1','2','3','4','5','6','7','8','9','0','-','=','q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','<','>',';',':','/',"'",'`']
    random_letter_place_store = 1
    while tat == True:
       letter_dict = {}
       clear()
       pri = random.randrange(1,2)
       lehn = len(prinline)
       if pri == 2:
          prinline.append(1)
       elif pri == 2 and lehn >= 2:
          prinline.remove(1)
       for item in pri:
          random_letter_place = random_letter_place_store
          random_letter_place = random_letter_place + random.randrange(-1,1)
          if random_letter_place < 0:
             random_letter_place = random.randrange(1,10)
             random_letter_place_store = random_letter_place
          while random_letter_place >= 0:
             getletter = random.choice(letter_list)
             letter_dict[random_letter_place] = getletter
             random_letter_place = random_letter_place - 1
          for place in letter_dict:
             print(letter_dict[place])
          if times == 0:
             break
          else:
             times = times - 1

if sat_choice == 'cyrcle' or sat_choice == 'cyrcle sat' or sat_choice == '2':
   boldness1 = '.'
   boldness2 = '-'
   boldness3 = '#'
   range1, range2 = (1, 4)
   def cyrcleprint(range1, range2, boldness1, boldness2, boldness3):
      c1 = 2 * 3.14159265358979323846264338327950288419 * range1
      c2 = 2 * 3.14159265358979323846264338327950288419 * range2
      print('c1 = ' + str(c1), 'c2 = ' + str(c2))
      pi1 = c1 / range1
      pi2 = c2 / range2
      print('pi1 = ' + str(pi1), 'pi2 = ' + str(pi2))

   cyrcleprint(range1, range2, boldness1, boldness2, boldness3)
   
if sat_choice == 'random' or sat_choice == 'random sat' or sat_choice == '3':
   import turtle
   from turtle import Screen
   t = turtle.Turtle()
   cont = True
   s = screen()
   color = {'red': 255, 'blue': 255, 'yellow': 255}
   sc = s.colormode(255)
   red = color.get('red')
   blue = color.get('blue')
   yellow = color.get('yellow')
   num = [1, 2, 3]
   while cont == True:
      if red > -1 and red < 256 and blue > -1 and blue < 256 and yellow > -1 and yellow < 256:
         red = red - random.choice(num)
         blue = blue - random.choice(num)
         yellow = yellow - random.choice(num)
         t.pencolor(color.get('red'), color.get('blue'), color.get('yellow'))
         t.ondrag(t.screen())
      else:
         red = red + random.choice(1,3)
         blue = blue + random.choice(1,3)
         yellow = yellow + random.choice(1,3)
         t.pencolor(red, blue, yellow)
         t.ondrag(t.screen())

else:
   cont = True
   function_list = ['Rotate()', 'Target()', 'Comms()', 'Lights()', 'Orbit()', 'Clock()', 'Cameras()', 'Supplies()', 'Warpjump()', 'Docking()', 'Scedule()', 'Power()', 'Reactor()', 'Sicurity()', 'Print()', 'Bots()', 'Logs()', 'Guns()', 'Priority()', 'Random()', 'Randomcamera()']
   times = int(input('Time: '))
   random_letter_place = int(times)
   random_letter_place_store = random_letter_place
   while cont == True:
      letter_dict = {}
      clear()
      random_letter_place = random_letter_place_store
      random_letter_place = random_letter_place + random.randrange(-1,1)
      if random_letter_place < 0:
         random_letter_place = random.randrange(1,10)
         random_letter_place_store = random_letter_place
      while random_letter_place >= 0:
         getletter = random.choice(function_list)
         letter_dict[random_letter_place] = getletter
         random_letter_place = random_letter_place - 1
      for place in letter_dict:
         print(letter_dict[place])
      if times == 0:
         break
      else:
         times = times - 0.00000000000000000001



      
   
