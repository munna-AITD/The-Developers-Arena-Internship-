#Object Oriented programming language philosphy and from that philosphy how do we code
#oops-> try to solve some real world issues with virtual world solution
#Python supports :- Procedural Programming -> Functional Programming -> Oops
#Class:-> blueprint for creating an object

#Object:->instance of class -> it gives the meaning to the class
class MyClass:
    num4 = 23
    # print(num4)

obj12 = MyClass()
print("The val is ",obj12.num4)

class Bank:
    bal = 0
    def checkBalanceAcc(a):
        print("Hello")

obj = Bank()
# obj.bal
obj.checkBalanceAcc()

#-------------------------------
class Student:
    def printMe(abc):
        print("Good Morning")

obj = Student()
obj.printMe()
#---------------------------------
#Many objects can be made for a class
class Sbi:
    var =10
    def printMe(self):
        print("Good Morning")

obj1 = Sbi()
print(obj1.var)
obj1.printMe()

obj2 = Sbi()
print(obj2.var)
obj2.printMe()
obj3 = Sbi()
print(obj3.var)

class MyClass:
    var = 10
    def display_value(self):
        print( "hello")

obj = MyClass()
obj.var
obj.display_value()
#--Self value is an object and stored in same memory as object
class Sbi:

    def printMe(self):
        # print("Good Morning")
        print("Self val inside class",self)

obj1 = Sbi()
print("Object1 value",obj1)
obj1.printMe()
# obj1.printMe()

obj2 = Sbi()
print("Object2 value",obj2)
obj2.printMe()

cus = Sbi()
cus.printMe()
#--------
class Sbi:
    def printMe(self,a,b):
        print("Good Morning",a + b)

a = 10
b=20
acc = Sbi()
acc.printMe(a,b)
#----
#Scope
# Class variables

class Sbi:
    var = 45

    def printMe(self):
        print(self.var)
        print("Good Morning")

a = 20
b = 90
acc = Sbi()
acc.printMe()
# acc.var
class Demo:
    var1 = 45

    def printMe1(self):
        self.num1 = 12
        print("The value 1 is",self.num1)

    def printMe2(self):
        self.num2 = 3
        print("The value 2 is",self.num2)

    def sum(self):
        print("The sum is ",self.num1 + self.num2)

obj = Demo()
print(obj.var1)
obj.printMe1()
obj.printMe2()
obj.sum()
