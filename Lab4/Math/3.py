import math
n, s = int(input("Input number of sides: ")), int(input("Input the length of a side: "))
p = n * s
a = s / (2 * math.tan(math.pi / n))
print(f"The area of the polygon is: {round((a * p) / 2)}")