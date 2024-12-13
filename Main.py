class Shape:
    def area(self , area):
        self.area = area


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


rect = Rectangle(4, 5)
print("Rectangle Area:", rect.area())

square = Square(3)
print("Square Area:", square.area())

