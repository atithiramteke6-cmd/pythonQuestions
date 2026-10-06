#Q1) create a class "Programmer" for storing information of few programmers working at microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Atithi",250000,440043)
print(p.name,p.salary,p.pin)

r = Programmer("Atirya",270000,440093)
print(r.name,r.salary,r.pin)

t = Programmer("Arya",430000,440073)
print(t.name,t.salary,t.pin)



#Q2) write a class "calculator" capable of finding square root of a number

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")


a = Calculator(4)
a.square()
a.cube()
a.squareroot()



#Q3) create a class with a class attribute a,create an object from it and set 'a' directly
#using object.a=0 does this change the class attribute

class Demo:
    a=4

o = Demo()
print(o.a)      #print class attribute because instance attribute is not present
o.a = 0    #instance attribute is set
print(o.a)      #print instance / object attribute because it is present

 #so answer is no class attribute doesn't change
print(Demo.a)

#Q4) Add a static method in problem 2, to greet user with hello.


class Calculator:

    @staticmethod
    def greet():
        print("Hello")

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")


a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()



#Q5)  write a  class Train which has methods to book a ticket,get status(no.of seats) and 
#get fare info of train running under indian railway.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no : {self.trainNo} is running successfully on time")

    def getFare(self,fro, to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222, 555)}")
        

t = Train(13899)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")


#Q6)  can you change the self parameter inside a class to something else(say "atithi").
#try changing self to "slf" or "atithi" and see the effects

'''so the ans is yes we can change self parameter to slf inside class else(say "atithi") also
'''


from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(atithi, fro, to):
        print(f"Ticket is booked in train no : {atithi.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no : {slf.trainNo} is running successfully on time")

    def getFare(slf,fro, to):
        print(f"Ticket fare in train no : {slf.trainNo} from {fro} to {to} is {randint(222, 555)}")
        

t = Train(13899)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")











