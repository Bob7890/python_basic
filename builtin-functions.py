# Builtins

# Built-in Sum Function
l = list(range(5))
ttl = 0
for i in l:
    ttl += i
print(ttl)

y = sum(l)
print(y)

# total largest / smallest
l = [5,2,6,1,3]
l.sort()
print(l[0], l[-1])

print(min(l))
print(max(l))

# from zero
x = [1, -8, -1, 5, 6]
for i in x:
    print(abs(i))

# round() method.
num = 3.534
print(round(num, 2))

# calculate grade point average.
def round_grade(grades):
    return round((sum(grades) / (len(grades))), 2)

# Pow Function
def exp(x, y):
    return x**y
print(exp(5, 2))

print(pow(5, 2))

# Print exponents (power)
def exp(root,power):
    """ root^power returns string of equation"""
    result = ""
    for i in range(power):
        result += f"{root} x "
    result = result[:-3]
    result += " = "
    rootPower = pow(root, power)
    result += f"{rootPower}"
    return result

print("power is: " + exp(3, 5))

# Builtin Ord Function ord(): unicode for one-character string
print(ord("a"))

# Function to take 2 arguments and return list of offset integers
def offset(letters, move):
    offsetList = []
    for letter in letters:
        offsetList.append(ord(letter) + move)
    return offsetList

offsetResult = offset('abcd', 3)
print(f"Offset {offsetResult}")

# chr(): Gets character from unicode number.
print(chr(97))

def offset_print(letters, move):
    """return string of offset chracters"""
    offsetResult = ""
    i = 0
    for letter in letters:
        offsetResult += chr(ord(letter) + move)
        i += 1
    return offsetResult

letterList = offset_print("Running", 5)
print(f"Letters = {letterList}")

# sorted Function: help(sorted): Returns new list sorted.

l = [5, 25, 1, -5, 0]
newList = sorted(l, reverse = True)
print(newList)

# sort based on a key (last item in each object)
l_2 = [[1, 5], [2, 3], [1, 4], [2, 2]]
def last(x):
    return x[-1]

newL2 = sorted(l_2, key=last)
print(newL2)

# Create a function that returns a 
# sorted list of lists by index 1 
def index(l):
    return l[1]
    
def sort_index(l_o_l):
    return sorted(l_o_l, key=index)

# numbering
l = ["Dog", "Cat", "Bird"]
newList = []
count = 0
for i in l:
    newList.append((0, i))
    count += 1
print(newList)

#enumerate Function:
newList2 = list(enumerate(l, 1))
print(newList2)

# Create a function that returns a
# enumerate object from the starting point
# which is given
def numbered(l,start):
    """Take l and start numbering with start argument"""
    return list(enumerate(l, start))

# Builtin Zip Function: help(zip): Build list from multiple lists.
x = list(range(3))
l = 'abc'

new = list(zip(l, x))
print(new)

# Create a function that returns a
# list of two lists zipped together
def zipped (l_1,l_2):
    """l_1 first then l_2"""
    return list(zip(l_1, l_2))

l_1 = [1, 2, 3, 4, 5]
l_2 = ["a", "b", "c", "d", "e"]
print(zipped(l_1, l_2))









