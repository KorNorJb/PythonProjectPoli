class Geometricfigure:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def Perimeter(self):
        pass

    def __str__(self):
        return f"Фигура: {self.__class__.__name__}, Цвет: {self.color}, Площадь: {self.area()}, Периметр: {self.Perimeter()}"


class Circle(Geometricfigure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

    def Perimeter(self):
        return 2 * 3.1415 * self.radius

    def __str__(self):
        return super().__str__() + f", Радиус: {self.radius}"


class Rectangle(Geometricfigure):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def Perimeter(self):
        return 2 * (self.height + self.width)

    def __str__(self):
        return super().__str__() + f", Длина: {self.height}, Ширина: {self.width}"


class Triangle(Geometricfigure):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def Perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return super().__str__() + f", Сторона 1: {self.side1}, Сторона 2: {self.side2}, Сторона 3: {self.side3}"

circle = Circle("Красный", 5)
rectangle = Rectangle("Синий", 4, 6)
triangle = Triangle("Зеленый", 3, 4, 5)
print(circle)
print(rectangle)
print(triangle)