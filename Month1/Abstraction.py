#Abstraction
#Hiding uneccessary details
#abstraction is not directly supported by python Import abc class
#inheritance and method overriding is must
#we cannot make the Abstract class object therefore if we want to fetch the abstract class method we need inheritance
from abc import ABC,abstractmethod

class Bank(ABC):

  def dataBase(self):
    print("DataBase connected")

  @abstractmethod
  def security(self):
    print("Hello")

class WebApp(Bank):
  def mobileApp(self):
    print("mobile App")

  def security(self):
    print("In child class")

obj = WebApp()
obj.dataBase()
obj.mobileApp()
obj.security()
#-----------------------------
from abc import ABC,abstractmethod

class Bank(ABC):
  def dataBase(self):
    print("DataBase connected")

  @abstractmethod
  def security(self):
    print("hjdsbvhjefivoerubgvio")
    print("Hello")

class WebApp(Bank):
  def mobileApp(self):
    print("mobile App")

  def security(self):
    print("In child class")

obj = WebApp()
obj.dataBase()
obj.mobileApp()
obj.security()
