#Python Polymorphism
#3 types:-
#1. Operator Overloading
#2. Method Overloading
#3. Method Overriding
#Method Overloading-> same class shares the same function name having different parameters

class MathOperation:

    def add(self,a,b):
        print(a + b)

    def add(self,a,b,c,d):
        print(a + b+c +d)

    def add(self,a,b,e):
        print(a + b*e)

    def add(self,a):
        print(a)


obj = MathOperation()
#obj.add(22,3)
#obj.add(1,2,3,4)
obj.add(2)
#--------------Method Overriding------------------
#Method Overriding ->More than 1 class that has exactly same function name and same no of parameters
#Inheritance is must
#useful when you want the child class to behave differently than the parent class in certain situation
class Sparrow:
    def behaviour(self,a,b):
        print("Sparrow can fly")

class Swan(Sparrow):
    def behaviour(self,r,s):
        print("Swans can swim")

obj = Swan()
obj.behaviour(2,7)

class Area:
    def __init__(self):
        pass
    def area(self,num):
        print("The number is ",3.17 *num*num)

class Square(Area):
    def print(self):
        print("Inside square")

    def area(self,l):
        print("The area is ",l*l)

class Circle(Area):
    def printMe(self):
        print("Inside Circle")


sq = Circle()
sq.area(2)
sq.printMe()

#obj = Circle()
#obj.area(2)

class Vehical:
  def wheel(self):
    print("The vehical has 4 wheel")

class Car(Vehical):
  def color(self):
    print("The color is black CAR")

class Bike(Vehical):
  def engine(self):
    print("The engine of bike BIKE")

  def wheel(self):
    print("Bike has two wheels")


class Truck(Vehical):
  def mirror(self):
    print("Truck has mirrors TRUCK")

obj1 = Car()
obj1.color()
obj1.wheel()

obj2 = Bike()
obj2.engine()
obj2.wheel()

obj3 = Truck()
obj3.mirror()
obj3.wheel()
