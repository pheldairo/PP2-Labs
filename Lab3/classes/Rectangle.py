from Square import Shape
class Rectangle(Shape):
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(int(input("Please enter the length of the rectangle: ")), int(input("Please enter the width of the rectangle: ")))
print(rectangle.area())