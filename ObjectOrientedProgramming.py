'''
solving a problem by creating object is one of the most popular approaches in programming.
this is called object oriented programming.
the concepts focuses on using reusable code (DRY principle)

class : classs is a blueprint of for creating object

object : an object is an instantiation of a class. when class is defined,a template(info)is 
defined.memory is allocated only after object instantiation. 
'''


class Employee:
    language = "py"            #salary and language is a class atributes which is belongs to the class Employee
    salary = 1200000

atithi = Employee()             #atithi is a object
atithi.name = "Atithi"
#here name is a object / instance atributes.

atithi.language = "Java"     #instance attribute take preferance over class attributes during assignment and retrival

print(atithi.name, atithi.salary, atithi.language)

atirya = Employee()             #atirya is a object
atirya.name = "Atirya"
#here name is a object / instance atributes.
print(atirya.name, atirya.salary, atirya.language)




#we identify the following in our program :
'''
Noun --> class --> Employee
Adjective --> Attributes -->name,age,salary
Verbs --> methods --> getSalary(), increment()
'''



#self parameter:   ham koi bhi method yani function banaye use self dena hi padta hai chahe ham use use kare ya na kare self ki jagah ham kuchh bhi likh sakte hai but self thoda jyada professional lagta isliye vahi
class Employee:
    language = "py"            #salary and language is a class atributes which is belongs to the class Employee
    salary = 1200000

    #__INIT__() constructor: this type of function or method which is start and end with __
#which is called as dunder method which call automatically.
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I am creating an object")

    def getInfo(self):  #self parameter:   ham koi bhi method yani function banaye use self dena hi padta hai chahe ham use use kare ya na kare
        print(f"the language is {self.language}. the salary is {self.salary}")


#agar ham chahte hai ki ham self na lagaye to hame use batana padega ki vo object nahi hai 
#aur vaha @staticmethod banana padega
    @staticmethod
    def greet():
        print("good night")

    # def greet(Self):
    #     print("good morning")

atithi = Employee("Atithi",20)
print(atithi.name,atithi.age)

atithi.language = "java"   #if the instance attribute is not present in this so language is print python
# atithi.getInfo()
Employee.getInfo(atithi)
atithi.greet()





