#Exception handeling : 
'''these are many built-in exceptions which are raised in python when something goes wrong.
Exception in python can be handled by using a try statement.the code that handles the 
exception is written in except clause.
when the exception is handled. the code flow continue without program interuption.'''

try:
    a = int(input("enter a number: "))
    print(a)

except ValueError as v:
    print(v)

except Exception as e:   #if we doesn't write except exception and in output we enter string not integer so our will crashed and give error.
    #if try block is not run then it move to except block
    print(e)

print("Thankyou!")


#Raising exception : 

a = int(input("enter a number : "))
b = int(input("enter second number : "))

if(b == 0):   
    raise ZeroDivisionError("Heyy our program is not meant to divide numbers by zero")
#we can't devide any number by 0 it gives us raise ZeroDivisionError .
#raise error can crashed the program lekin kabhi kabhi program crash bhi hona chahiye lyu ki agar programmer galti kare to use pata chale ki hamne bahot serious mistake ki hai
else:
    print(f"The division a/b is {a/b}")





