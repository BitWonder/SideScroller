import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

length = int(input('Length of password(Max Of 94): '))

x = True

all = lower + upper + num + symbols

output = ['Password is :', ' ']

temp = random.sample(all,length)

password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation

passes = "".join(random.sample(all,length))

print(password)
