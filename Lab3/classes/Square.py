class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


square = Square(int(input("Please enter the length of the square: ")))
print(square.area())