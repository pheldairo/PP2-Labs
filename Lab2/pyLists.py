#Initialize a list
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

# Can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Type of list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Access items
print(thislist[1])
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])
# Range of indexes
print(thislist[2:5])
# From beginning but not including the end
print(thislist[:4])
# Same, but reversed meaning
print(thislist[2:]) 
# Range of negative indexes
print(thislist[-4:-1])
# Check if item exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Removes the first occurrence of the specified value

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()

# Output a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
for i in range(len(thislist)):
  print(thislist[i]) 
while i < len(thislist):
  print(thislist[i])
  i = i + 1
[print(x) for x in thislist]

# Compherensions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
newlist = [x for x in fruits if x != "apple"] 
newlist = [x for x in range(10)] 
newlist = [x for x in range(10) if x < 5] 
newlist = [x.upper() for x in fruits] 
newlist = ['hello' for x in fruits] 
newlist = [x if x != "banana" else "orange" for x in fruits] 

#Sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Numeric
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customizing
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case sensitivity
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Reversing
thislist.reverse()
print(thislist)

# Copying
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Joining
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
# OR

for x in list2:
  list1.append(x)

print(list1) 