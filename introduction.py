name = "Bob Demers"

print(name)

for letter in name:
    print(letter*3)

def hello():
    """This function prints hello"""
    
    print("hello")
    print()
    print("How are you?")


def hellox2():
    hello()
    hello()

hellox2()

f = 1.2

l = []
l.append(f)
l.append(name)

print(l)

d = {}

d[1] = "one"
d[2] = "two"
d["poo"] = "three"

print(d)

t = (1, 4, 3)

print(t)

x = 1

while x < 10:
    print(x)
    x += 1
    
print(x)

x = 10

if x < 10:
    print("Yes")
else:
    print("No")

x = 4
if x%2 == 0:
    print("Is Even")
else:
    print("Is Odd")

score = [3, 4, 5]


def is_even(list):
    """Test number in list to see if even"""
    for number in list:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")

is_even(score)

r = range(10)

for i in range(2, 11, 2):
    print(i)

name = "Samuel"
print(name[1:4:2])

print(name[:6:2])

print(name[::3])

print(name[0:5:2])

letters = "abcdefghijk"
print(letters[0:5:2])

import math

def double(x):
    return x * 2

new = double(5)
print(new)







