from math import pi

class Circle:
    def __init__(self, radius):
        self.set_radius(radius)   
    def perimeter(self):
        return self.__radius * pi * 2
    def area(self):
        return self.__radius ** 2 * pi
    def get_radius(self):
        return self.__radius  
    def set_radius(self, radius):
        self.__radius = float(radius)      
    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.area(), self.perimeter())

def main():   
    radius = input("Radius of circle: ")        
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)   
    print(circle)

main()