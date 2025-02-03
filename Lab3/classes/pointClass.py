class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def show(self):
		print(f'Your point at ({self.x},{self.y}) coordinates')

	def move(self, z):
		z = int(z)
		self.x += z
		self.y += z

	def dist(self, other_point):
		dis = ((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**(0.5)
		print(f'Distance between two points is {round(dis, 2)}')

point1 = Point(int(input("X coordinate of the first point: ")), int(input("Y coordinate of the first point: ")))
point2 = Point(int(input("X coordinate of the second point: ")), int(input("Y coordinate of the second point: ")))
move = int(input("The distance to move both points: "))
point1.show()
point2.show()

point1.dist(point2)

point1.move(move)

point2.dist(point1)