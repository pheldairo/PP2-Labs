import math

def volume(radius):
    C = (4/3) * (math.pi * (radius ** 3))
    print(round(C))

radius = int(input("Enter radius of the sphere: "))
volume(radius)