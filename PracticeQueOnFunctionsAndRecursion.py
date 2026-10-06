#Q)1 - using function find greatest number


# def greatestNumber(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c

# a = int(input("enter no. : "))
# b = int(input("enter no. : "))
# c = int(input("enter no. : "))

# print(greatestNumber(a,b,c))     #function call


#Q)2- convert celsius to fahrenheit using function

#formula of celsius to fahreheit: c/5 = (f-32)/9 = c = 5*(f-32)/9

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("enter temperature in F : "))
# c=f_to_c(f)
# print(f"{round(c,2)}°C")       #round function is used to give 2 digits after decimal point


#Q)3 - prevent apython print() function to print a new line at the end

# print("a")
# print("b")
# print("c", end = "")   #this end="" used to avoid next line
# print("d" ,end ="")


#Q)4- write a recursive function to calculate the sum of first n natural numbers.

'''
sum(n) = 1+2+3+4+....+(n-1) + n
formula of caluculate sum of n natural numbers:
sum(n) = sum(n-1) + n'''


# def sum(n):
#     if (n==1):
#         return 1
#     return sum(n-1) + n

# n=int(input("enter number : "))

# print(sum(n))



#Q)5 - write a function to print first n lines of the following pattern : 
'''

***
**
*
for n = 3
'''

# def pattern(n):
#     if(n==0):
#         return          #agar ye upar vali base condition true ho gayi to aage ka program run nahi hoga vahi pe stop ho jayega

#     print("*" * n)
#     pattern(n-1)

# pattern(3)



#Q)6 - write a function to convert inches to cms

'''
inches to cms coversion ke liye 2.54 se multiply karna padta hai'''

# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("enter value in inches : "))

# print(f"the corresponding value in cms is {inch_to_cms(n)}")



#Q)7 - write a function to remove a given word from a list and strip it at the same time



# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))          #strip function is used to remove a word from backward and forward
#     return n
       
# l = ["Atithi", "Anaya", "samya", "Anu", "ya"]

# print(rem(l,"ya"))


#Q)8 - write a function to print multiplication table of a given number

def mult(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

mult(6)

