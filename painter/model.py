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