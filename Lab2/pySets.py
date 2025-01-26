# Initialize a set 
myset = {"apple", "banana", "cherry"}
print(myset) 

# Duplicates are not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Length of a set
print(len(thisset))

# Data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

# Type of a set
print(type(myset))

# Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

# Access
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
print("banana" in thisset) 
print("banana" not in thisset) 

# Add items
thisset.add("orange")

print(thisset) 

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) 

# Add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset) 

# Remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) 

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # Returns the removed item (Random)
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # Will raise an error because the set no longer exists

# Loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

# Join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

set3 = set1 | set2
print(set3) 

set1 = {"a", "b", "c"} # Multiple sets
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
myset = set1 | set2 | set3 |set4
print(myset) 

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y) # Set + Tuple
print(z) 

# Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) 

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3) 

set3 = set1 - set2
print(set3) 

set1.difference_update(set2)
print(set1) 

# Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3) 