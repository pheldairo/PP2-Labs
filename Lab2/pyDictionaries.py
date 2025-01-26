# Creating a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print a specific value
print(thisdict["brand"])

# Length
print(len(thisdict))

# Type
print(type(thisdict)) 

# Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Accessing Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# Keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 

# Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 

# Items 
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 

# Check if Key Exists
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

# Change Values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"year": 2020})

# Adding Items
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"color": "red"}) 

# Removing Items
thisdict.pop("model")
print(thisdict) 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 

# Clear dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) 

# Loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) 
for x in thisdict:
  print(thisdict[x]) 
for x in thisdict.values():
  print(x) 
for x in thisdict.keys():
  print(x) 
for x, y in thisdict.items():
  print(x, y) 

# Copy a Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
print(myfamily["child2"]["name"])  # Access the dictionary 

for x, obj in myfamily.items(): # Or just loop through it
  print(x)

  for y in obj:
    print(y + ':', obj[y])
