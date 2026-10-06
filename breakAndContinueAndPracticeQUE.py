# for i in range(100):
#     if(i == 34):
#         break            #exit the loop right now
#     print(i)


# for i in range(10):
#     if(i == 0):
#         continue           #skip thi iteration
#     print(i)



#pass - thodi der ke bad vo kam krna hai (means pass is a null statement in python its instruct to do nothing)

# for i in range(645):
#     pass           #after sometimes we run this for loop first we run below while loop so that purpose we use pass



# i = 0
# while(i<=45):
#     print (i)
#     i += 1




#practice questions

#Q)1  - print table using for loop

# n = int(input("enter a number : "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


#Q)2  -  greet all the person names stored in list 'l' and which starts with S

# l = ["Atithi", "Sakshi", "Bhumi", "Sahil"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello , {name}")



#Q)3 - print table using while loop

# n = int(input("enter a no. : "))

# i = 1
# while(i<=10):
#     print(f"{n} * {i} = {n*i}")
#     i+=1


#Q)4 - no. is prime or not

# n = int(input("enter a no. : "))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("no. is not prime")

#         break

# else:
#     print("no. is prime")



#Q)5 - calculate sum of first n naturnal numbers

# n = int(input("enter a no. : "))
# i=0
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)


#Q)6- calculate the factorial of a given number using for loop

#ex : 5! = 1*2*3*4*5

# n = int(input("enter a no. : "))
# product = 1           #jab product (multiplication) karte hai to 1 se initialize karte hai aur sum karte hai to 0 se initialize karte hai

# for i in range(1,n+1):
#     product = product * i

# print(f"factorial of {n} is {product}")


#Q)7 - print star pattern
'''  *
    ***
   ***** 
for n=3'''


# n = int(input("enter a no . : "))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("") #for adding new line . don't use print("\n") this add extra new line which is not needed


#Q)8- print star pattern
'''
*
**
***
for n=3
'''
# n = int(input("enter a no . : "))

# for i in range(1,n+1):
#     print("*"*i, end="")
#     print("") 


#Q)9- print the star pattern
'''
***
* *
***
for n=3
'''

# n = int(input("enter a no . : "))

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")


#Q)10- print table in teversed order

n = int(input("enter a no . : "))
  
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")

















