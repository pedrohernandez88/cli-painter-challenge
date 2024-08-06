import matplotlib.pyplot as plt
import math
import pickle

class Point:
    def _init_(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle:
    def _init_(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
    
    def area(self)-> float:
        return math.pi * self.radius ** 2
    
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def _str_(self):
        return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"
    
class triangle:
    def _init_(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
    
    def area(self)-> float:
        return abs((self.point_1.x * (self.point_2.y - self.point_3.y) +
                    self.point_2.x * (self.point_3.y - self.point_1.y) +
                    self.point_3.x * (self.point_1.y - self.point_2.y)) / 2)
    
    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()
    
    def _str_(self):
        return f"Triangle with vertices at ({self.point_1.x}, {self.point_1.y}), ({self.point_2.x}, {self.point_2.y}), and ({self.point_3.x}, {self.point_3.y})"
    
