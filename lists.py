# Lists
l_1 = [1, 4, 6]
l_2 = [3, "Sam", 1.2]

print(l_1, "len = ", len(l_1))
print(l_2, "len = ", len(l_2))

# add lists together
l_3 = l_1 + l_2
print(l_3)

# help(list.extend) - get help on list.extend method

# extend method - adds list 2 to end of list 1
l_1.extend(l_2)
print(l_1)

# help(list.append) - append object to end of the list.

# add '5' string to l_1
l_1.append('5')
print(l_1)

# add list to l_2
l_2.append([])
print(l_2)

# appends entire list l_1 as one object into list l_2
l_2.append(l_1)
print(l_2)

# list index, help(list.index), finds first index of value
l_1 = [1, 4, 6, '5']
print(l_1.index(4))   # output 1, finds 4 at index 1

# list pop method, help(list.pop), removes and returns item at index.
l_1 = [1, 4, 6]
l_2 = [3, "Sam", 1.2, []]
empty = l_2.pop()
print(empty)
print(l_2)

# pop out index 1 (ie 4)
item = l_1.pop(1)
print(item)

# list insert method
l_2.insert(0, "Fish")
print(l_2)

# list sort method, sort in-place in ascending order. sort(*,key, reverse)
l_1 = [1, 4, 6, 3, 5, 7, 2]
l_1.sort()
print(l_1)

# list count method, return number of occurances of value. count(value, /)
l_1 = [1, 4, 4, 3, 3, 1, 2, 4, 4, 4]
print(l_1.count(4))

# list remove method, remove(valu, /), removes first occurance of value
l_1.remove(1)
print(l_1)
l_1.remove(3)
print(l_1)

# list reverse method, reverse list in-place
l_1 = [1, 4, 4, 3, 3, 1, 2, 4, 4, 4]
l_1.reverse()
print(l_1)

# list clear method, remove all items from list
l_1.clear()
print(l_1)

# list copy method, returns shallow copy of the list
l_1 = [1, 4, 4, 3, 3, 1, 2, 4, 4, 4]
l_3 = l_1.copy()
print(l_3)

# change list with index
l_2 = [3, "Sam", 1.2]
l_2[0] = "Tom"
print(l_2)

# wrap a string with list, creates a list with each letter each index
s = "janbjonbvoi"
t = "samiam"
new_s = list(s)
print(new_s)
new_t = list(t)
print(new_t)





