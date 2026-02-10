#Encapsulation
#-> Wrapping up of data and functions together in a class as a single unit
#-> Involves restricting direct access to data :- Public and Private
class Results:

  def __init__(self):
     self.color = "blue"
     self.__marks = 456#Private
     self.name = "Rahul"
     self.rollNo = 23
     print(self.color)

  def percentage(self):
    print(self.__marks)
    result = (self.__marks/500)*100
    print("The pecentage is ",result)
    print(self.color)

obj = Results()
obj.percentage()
obj.__marks
# print(obj.marks)
# print(obj.rollNo)
# print(obj.color)
######---------------------------
class Results:

  def __init__(self):
     self.color = "blue"
     self.__marks = 456#Private
     self.name = "Rahul"
     self.rollNo = 23
     print(self.color)

  def percentage(self):
    print(self.marks)
    result = (self.marks/500)*100
    print("The pecentage is ",result)
    print(self.color)

obj = Results()
obj.percentage()
# obj.marks
print(obj.__marks)
print(obj.rollNo)
print(obj.color)
##########----------------------------
class Private:
  def info(self):
    self._uid = "23AA"#Protected
    self.__password ="aa@12"
    print("Method executed")

  def display(self):
    print("UID is ",self._uid)

class Protected(Private):
  def print(self):
    print("The value ",self._uid)
    print("The password is ",self.__password)

obj = Protected()
obj.info()
obj.display()
print(obj._uid)
obj.print()
# obj.__password