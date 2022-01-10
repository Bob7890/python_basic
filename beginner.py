
"Sam" + "uel"

f = "Sam"

l = "uel"

full = f + l

print(full)

name = "Samuel"

print(name[-4])

print(name[3])

numbers = "2468"

y = int(numbers[1])

print(y)

print(name.lower())

print(name.upper())

myName = "bob demers"
print(myName.title())

numbers = "2468"
print("2" in numbers)

l = [1, 2, 3]
print(1 in l)

print(len(l))

print(myName, "length is", len(myName))

r = range(10)
for i in r:
    print(i)

print("bob", "is", 20)

for i in range(3):
    print("I is", i)
    for j in range(3):
        print(" J is", j)

# Variable Swap
a = 1
b = 2
a, b = b, a
print(a, b)

# Boolean Values
1 == True
False == 0

# Keyword Return
def name():
    return "Sam"

print(name())

# elif
def metal(x):
    if x == 1:
        return "Gold"
    elif x == 2:
        return "Silver"
    else:
        return "Bronze"
    
print(metal(2))

# Multiple function arguments
def total(x, y):
    ### add x and y
    return x + y

print(total(3, 4))
print(total(1, 4))




