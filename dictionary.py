# dictionary (dict), key value mapping.

dict()
{}

# create dictionary
d_1 = {"A": 4, "B": 6, "C": 9, "D": 5, "F": 2}

print(d_1)

d_2 = dict(A=4,B=6,c=9,d=5,f=2)
print(d_2)

d_3 = dict([("A", 4), ("B", 6), ("C", 9), ("D", 5), ("F", 2)])
print(d_3)

x = ['A', 'B', 'C', 'D', 'F']
y = [4, 6, 5, 2]
d_4 = dict(zip(x, y))
print(d_4)

# dict.fromkeys
d_5 = dict.fromkeys(x)
print(d_5)

# set d_6 to d_5 but with default values of 0
d_6 = dict.fromkeys(x, 0)
print(d_6)

#  keys() method : help(d_1.keys)
keys = d_1.keys()
print(type(keys))

#  get() method: help(d_1.get("A")), returns the value
value = d_1.get("A")
print(value)

#  alt get() method
print(d_1["A"])

#  values() method: help(dict.values), gets the values from the dictionary.
values = d_1.values()
print(values, type(values))

# items() method: help(dict.items), items in dictionary in tuples.
print(d_1.items())

# Dictionary Membership, in the dictionary.
print("A" in d_1) # is A in d_1 dictionary.
print("G" in d_1) # is G in d_1 dictionary.

# Loop through Dictionary
for key in d_1:
    print(key) # gets only keys.

for value in d_1.values():
        print(value) # gets only values

for i in d_1.items():
        print(i) # tuple of items

# unpacking items
for key, value in d_1.items():
    print(key, value) # prints key and value 

# pop() method: help(dict.pop), remove specific key and return corresponding value.
value = d_1.pop("B")
print(value)
print(d_1)

# popitem() method: help(dict.popitem), remove and return (key, value) pair as 2-tuple
d_2.popitem()
item_D = d_2.popitem()
print(item_D)

# setdefault() method: help(dict.setdefault), insert key with a value of default if key is not in dictionary.
# cannot hcange the value of a key if already inserted.
print(d_3)
d_3.setdefault("Drop")
d_4.setdefault("A")
d_4.setdefault("Drop", 0)

# update() method, help(dict.update), updates a key in the dictionary.
print(d_4)
d_4.update(A=5)
print(d_4)
d_4.update(B=8,WF=5)
print(d_4)

# copy() method, help(dict.copy): shallow copy of dictionary.
print("d4 = ", d_4)
d_6 = d_4.copy()
print("d6 = ",d_6)

# clear() method, help(dict.clear): removes all items from dictionary.
d_6.clear()
print("d6 = ",d_6)

# another way to create empty dictionary.
d_8 = dict()
print(d_8)

# another way to create empty dictionary.
d_9 = {}

# add key/values to dictionary.
d_8["Sam"] = 44
d_8["Tom"] = 33
print(d_8)

d_9["Count"] = 0
d_9["Sum"] = 0

# increment values assigned to keys in the dictionary.
for i in range(25):
    d_9["Count"] += 1
    d_9["Sum"] += i
print(d_9)

