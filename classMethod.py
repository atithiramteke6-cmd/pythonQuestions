#a class method is a method which is bound to the class and not the object of the class.
#@classmethod decorator is used to create a class method

'''
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e=Employee()
e.a=45

e.show()
'''



#property decorator

class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(Self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



e=Employee()
e.a=45

e.name = "Atirya Shende"
print(e.fname,e.lname)

e.show()