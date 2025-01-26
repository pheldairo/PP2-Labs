# For in array
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# For in string
for x in "banana":
  print(x)

# break example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# continue example
for x in fruits:
  if x == "banana":
    continue
  print(x)

# range function in for loop
for x in range(6):
  print(x)

for x in range(2, 30, 3):
  print(x)

# else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

# Pass statement
for x in [0, 1, 2]:
  pass