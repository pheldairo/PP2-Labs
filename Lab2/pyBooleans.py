print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

# Will return true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Functions can return a bool
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

#Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) 