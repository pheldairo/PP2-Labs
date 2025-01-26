# Initialize a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Length of a tuple
print(len(thistuple))

# One item tuple
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Access tuple items
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple # Note: Printing a tuple after deleting will raise an error because the tuple no longer exists 

# Unpack tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Looping
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
for i in range(len(thistuple)):
  print(thistuple[i]) 
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

# Join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

# Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 