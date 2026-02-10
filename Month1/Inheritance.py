#Inheritance
#classes inherits the property from another classes Parent Class/Base class -class being 
# inherited from Child Class/Derived class -> class that inherits properties from another class
class parent():
    num = 10
    def parentFun(self):
        print("Inside parent class")

class child(parent):
    var = "hello"
    def childFun(self):
        print("Inside child function")

obj = child()
print(obj.childFun())
print(obj.var)
print(obj.num)
#---Here child function is most workable function
class GrandFather():
    var1 = 20
    def GrandParentFun(self):
        print("Inside GrandFather ")
class parent(GrandFather):
    var2 = 10
    def parentfun(self):
        print("Inside parent class")
class child(parent):
    var= "hello"
    def childfun(self):
        print("Inside child class")
class child2(child):
     def child2Fun(self):
        print("Inside child 2 class")

obj = child2()
obj.child2Fun()
obj.childfun()
print(obj.var)
print(obj.var1)
print(obj.parentfun())

#-------Multiple class-------------
class Mother:
    def motherClass(self):
        print("Inside motherClass")

class Father:
    def fatherClass(self):
        print("Inside fatherClass")

class Child(Mother,Father):
     def childFun(self):
        print("Inside child class")

obj = Child()
obj.motherClass()
obj.fatherClass()
obj.childFun()

f1 = Father()
f1.fatherClass()

m1 = Mother()
m1.motherClass()

class Parent:
    num =10
    def parentFun(self):
        print("Inside Parent class")

class Child1(Parent):
    var = "hello"
    def child1Fun(self):
        print("Inside child class")

class Child2(Parent):
     def child2Fun(self):
        print("Inside child 2 class")


# P1 = Parent()
# P1.parentFun()
# P1.child1Fun()

c1 = Child1()
c1.parentFun()
c1.child1Fun()
# c1.child2Fun()

c2 = Child2()
c1.parentFun()
c2.child2Fun()
