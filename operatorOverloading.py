#operator overloading

# class Number:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self,num):      #operator overloading constructor/function to addition 2 numbers
#         return self.n+num.n

#     def __sub__(self,num):
#         return self.n-num.n

#     def __mul__(self,num):
#         return self.n*num.n

#     def __truediv__(self,num):
#         return self.n/num.n

#     def __floordiv__(self,num):
#         return self.n//num.n


# n = Number(4)
# m = Number(5)

# print(n+m)
# print(n-m)
# print(n*m)
# print(n/m)
# print(n//m)




#Practice questions 

#Q1) create a class(2-D vector) and use it to create another class representing a 3-D vector

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"the vector is : {self.i}i + {self.j}j")


# class ThreeDVector(TwoDVector):     #inherit the property of TwoDVector also
#     def __init__(self,i,j,k):
#         super().__init__(i,j)       #to firstly set i and j
#         self.k = k

#     def show(self):
#         print(f"the vector is : {self.i}i + {self.j}j + {self.k}k") 


# a = TwoDVector(1,2)
# a.show()
# b = ThreeDVector(5,2,3)
# b.show()



#Q2)  create a class pets from class 'Animals' and further create a class 'Dog' from pets
#Add a method 'bark' to class 'Dog'

# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d = Dog()
# d.bark()



#Q3)  create a class 'Employee' and add salary and increment properties to it
#write a method salaryAfterIncrement method with @property decorator with a setter which
#changes the value of increment based on the salary.

# class Employee:
#     salary = 254
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.increment =  ((salary/self.salary) -1) *100

#     # def show(self):
#     #     print(f"the salary is: {self.salary} and increment by : {self.increment}")

# e = Employee()
# # print(e.salaryAfterIncrement)

# e.salaryAfterIncrement = 280.8
# print(e.increment)
#e.show()



#Q4) write a class 'Complex' to represent complex numbers ,along with overloaded operators '+' and '*'
#which adds and multiplies them.

# class Complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i


#     def __add__(self,c2):
#         return Complex(self.r + c2.r, self.i + c2.i)

#     def __mul__(self,c2):
#             real_part = self.r * c2.r - self.i * c2.i
#             imag_part = self.r * c2.i + self.i * c2.r
#             return Complex(real_part, imag_part)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c1 = Complex(1,2)
# c2 = Complex(3,4)
# print(c1+c2)
# print(c1 * c2)



#Q5) write a class vector representing a vector of n dimensions.overload the + and + operator
#which calculates the sum and the dot(.) product of them.

# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self,other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self,other):
#         result = self.x * other.x + self.y * other.y +  self.z * other.z
#         return result

#     def __str__(self):
#         return f"Vector({self.x} , {self.y} , {self.z})"

# #test the implimentations
# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)  

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)



#Q6) write __str__() method to print the vector as follows :
#7i + 8j + 10k
#assume vector of dimension 3 for this problem.

# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self,other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self,other):
#         result = self.x * other.x + self.y * other.y +  self.z * other.z
#         return result

#     def __str__(self):
#         return f"Vector({self.x}i + {self.y}j + {self.z}k)"

# #test the implimentations
# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)  

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)



#Q7) override the __len__() method on vector of problem 5 to display the dimension of their vector
    
class Vector:
    def __init__(self,list):
        self.list=list
       # self.x , self.y, self.z = list

    

    def __len__(self):
        return len(self.list)

#test the implimentations
v1 = Vector([1,2,3])
print(len(v1))








