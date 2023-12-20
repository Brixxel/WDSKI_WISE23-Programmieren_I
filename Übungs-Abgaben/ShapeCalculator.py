from abc import ABC, abstractclassmethod
import math

# Author @Tom ; @Felix ; @Gina
# Version 1.0
# Date 12.12.2023

# ein einfacher Rechner zum vergleichen von verschiedenen simplen geometrischen Figuren
# weil sich unverstädnlich ausgedrückt wurde, müssen obsoleterweise auch hässliche Dreiecke ohne rechten Winkel berücksichtigt werden

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def scope(self):
        pass   

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Shape):
            o: Shape = __o
            return self.area() < o.area()
        return False
    
    def __gt__(self, __o: object) -> bool:
        if isinstance(__o, Shape):
            o: Shape = __o
            return self.area() > o.area()
        return False
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Shape):
            o: Shape = __o
            return self.area() == o.area() and self.scope() == o.scope() and type(self) == type(o)
        return False
   
    ## elegante Lösug, aber nicht statisch :/
    def __add__(self, __o: object) -> float:
        if isinstance(__o, Shape):
            o: Shape = __o
            return self.area() + o.area()
        return False
    
    ## Lösung als statische Methode der eine Liste Übergeben wird
    @staticmethod
    def sum_areas(shapes: list):
        sum_areas_calc = 0
        for i in range(0, len(shapes)):
            sum_areas_calc += shapes[i].area()
        return sum_areas_calc



class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Flasche Eingabe Parameter")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s *(s-self.a)*(s-self.b)*(s-self.c))
    
    def scope(self):
        return self.a + self.b + self.c
    
    def __str__(self) -> str:
        return (f"Dreieck: Seite a: {self.a}; Seite b: {self.b}; Seite c {self.c}")
    

class Rectangle(Shape):
    def __init__(self, a: float, b: float) -> None:
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            print("Flasche Eingabe Parameter")

    def area(self):
        return self.a * self.b
    
    def scope(self):
        return 2*self.a + 2* self.b
    
    def __str__(self) -> str:
        return (f"Rechteck: Seite a: {self.a}; Seite b: {self.b}")
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        if radius > 0:
            self.radius = radius
        else:
            print("Flasche Eingabe Parameter")

    def area(self):
        return math.pi * (self.radius**2)
    
    def scope(self):
        return math.pi * self.radius * 2

    def __str__(self) -> str:
        return (f"Kreis: Radius a: {self.radius}")
    
class Iso_Triangel(Rectangle):
    def __init__(self, a: float, b: float) -> None:
        if a > 0 and b > 0:
            self.a = a
            self.b = b
            self.c = b
        else:
            print("Flasche Eingabe Parameter")

class Square(Rectangle):
    def __init__(self, a: float,) -> None:
        if a > 0:
            self.a = a
            self.b = a
        else:
            print("Flasche Eingabe Parameter")




#### #### #### Hier wird gespielt #### #### ####

Dreieck = Triangle(3, 4, 5)

Viereck = Rectangle(4, 3)

print(Dreieck.area())
print(Dreieck.scope())

print(Dreieck < Viereck)

print(Dreieck+Viereck)

print(Shape.sum_areas([Dreieck, Viereck]))