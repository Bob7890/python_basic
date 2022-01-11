# Strings: immutable.

x = "asdfnmlk"
y = 'asdfnmlk'
print(x, y)

# concatenate
z = x + y
print(z)

# String Sub-string Membership
print("a" in x)
print("as" in x)

# index() method: help(str.index) returns lowest index in S where found.
i = x.index("f")
print(i)

x += "a"

a_2 = x.index("a", 1)
print(a_2)

# count() method: help(str.count) return number of non-overlapping occurances of substring
value = x.count("a")
print(value)

y = "aabbnncfggghaa"
print(y.count("aa"))

# returns all indices where found sub in letters.
def index_all(letters,sub):
    index = []

    location = 0
    occurances = letters.count(sub)
    while occurances > 0:
        location = letters.index(sub, location)
        index.append(location)
        occurances = letters.count(sub, location + 1)
        location += 1
    return index

myindex = index_all("abcabcdef", "ab")
print(myindex)

# find() method: Similar to index but returns -1 if not found.
x = 'aabbnncfggghaa'
print(x.find('abd'))
print(x.find('aa', 1))

# split() method: help(str.split): returns list of words in string using delimiter.
sen = "hi i'm Sam, nice to meet you"
tokens = sen.split(",")
print(tokens)

# join() method: help(str.join): Concatenate any number of strings.
print(",".join(tokens))
print("-".join(x)) #dashes between each letter in string x.

# String List Split
letter_1 = list(x)
print(letter_1)

letter_2 = list(sen)
print(letter_2)

# Test string ending in "ing"
x = "jumping"
y = "happy"
r = "running"
tests = [x, y, r]
def if_ing(test):
    print(test[-3::1] == "ing")

for test in tests:
    if_ing(test)

# endswith() method: help(str.endswith).
print(x.endswith("ing"))

# Check if string starts with vowel
def Starts_with_Vowel(word):
    l = [ "a", "e", "i", "o", "u" ]
    for let in l:
        if Starts_with(word, let):
            return True
    return False

def Starts_with(word, letter):
    if word[0] == letter:
        return True
    else:
        return False

# startswith() method: help(str.startswith).
print(x.startswith("ju"))

# replace() method: help(str.replace).
x = "truck and the road"
y = x.replace("a", "_")
print(y)

# replace first 3 occurances of space with underscore
z = x.replace(" ", "_", 3)

# string quotes, tabs and new lines
s = 'hello'
d = "hi i'm Sam"
e = 'hi i\'m Sam\nCan you help me?'
print(e)

# strip() method: removes trailing whitespace removed.
sen = "   from this person    "
print(sen.strip())

# String is Methods
name = "Sam"
print(name.islower())

i = "1234"
print(i.isdigit())

print(name.isalpha())

both = "th234asdf"
print(name.isalnum())
print(i.isalnum())
print(both.isalnum())
print(both.isdigit())

# format() method
print("Sam is " + str(44) + " years old.")
name = "Sam"
age = 44
sen = "{} is {} years old.".format(name, age)
print(sen)

# f-string method
print(f"Hi {name}, is {age} years old.")

print(f"{name:6} is {age:03} years old")

def fstring(first,second):
    return f"{second} I'm here what do you {first}"

print(fstring("Bob", "James"))

# center() method. Adds padding to center the string (with filler char)
print("test:" + name.center(8) + ":test")
print(name.center(7, "*"))

# partition() method. Partitions string into three parts with separator.
sen = "Hi how are you?"
print(sen.partition("are"))

sen = "Today is a good day"
print(sen.partition("a"))

# ljust() method: return a left justified.
name = "Sam"
print(name.ljust(7, "*"))

# lstrip() method: Return copy of string with leading whitespaces removed
name = "   Sam"
print(name.lstrip())

# rfind() method: Returns highest index of substring.
letters = "abcdabc"
print(letters.find("a"))
print(letters.rfind("a"))

# rsplit() method: split but in reverse starting at end of the string.
sen = "Today is a good day"
print(sen.rsplit())
print(sen.rsplit("a", 1))

# rjust() method: right-justified string.
name = "Sam"
print(name.rjust(8, "*"))

#rindex() method: Return the highest index of substring.
letters = "aeiouatbi"
print(letters.rindex("a"))
print(letters.index("a"))

# right justify word so final string length is % 3 = 0. Add "_" to front of string.
def Pre_padding(word):
    if len(word) % 3 == 0:
        return word.rjust(len(word)+3, "_")
    elif len(word) % 3 == 1:
        return word.rjust(len(word)+2, "_")
    else:
        return word.rjust(len(word)+1, "_")

# rstrip() method: Return copy of string with trailing whitespaces removed.
name = "Sam       "
print(":" + name.rstrip() + ":")

# rpartition() method: Partiion string into three parts, starting search from the right.
sen = "Today is a good day"
print(sen.partition(" "))
print(sen.rpartition(" "))






