#*******8Constructors***********
#a self-involking function which is called as soon as we create an object
#automatically called when we create object of classct used to initialze class variables
class Student:
    def __init__(self):
        print("Inside Constructor")

    def myFun(self):
        print("Hello")
obj = Student()
print(obj)

class girl():
    def __init__(self, age):
        print("The age is ", age)
    def printMe(self,name):
        print("The name is ", name)

obj1 = girl(24)
obj1.printMe("Tanisha")
############
class girl():
    def __init__(self):
        self.age = 24
    def printMe(self):
        #self.age = 24
        self.name="Manisha"
        print(f"The name of girl is {self.name} and age {self.age}")
obj2 = girl()
print(obj2.printMe())

#---------------------
class Bank():
    def __init__(self):
        self.bal = 0
    def deposite(self, amount):
        self.bal = self.bal + amount
    def debit(self, amount):
        self.bal = self.bal-amount
    def display(self):
        print(f"The final balance is ", self.bal)
obj = Bank()
obj.deposite(10)
obj.display()
obj.deposite(100)
obj.display()
obj.debit(50)
obj.display()
