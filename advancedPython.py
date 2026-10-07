#walrus operator(:=)  -
# the walrus operator introduced in python 3.8,allows you to assign values
#to variables as part of an expression .this operator , named for its resemblance to the eyes 
#and tusks of a walrus , is officially the "assignment expression"

#using walrus operator
if(n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

    #output : list is too long (5 elements , extected <= 3)



#types definition in python : 
#types hints are added using the colon (:) syntax for variable 
#and the -> syntax for function return types.
#pythons typing modules provides more advanced type hints , such as list,tuple,dict and union
#you can import list,tuple and dict types from the typing modules.

from typing import List,Tuple,Union

n : int = 5
name : str = "Atirya"

def sum(a:int,b:int) -> int:     #int isliye likha kyu ki ans integer chahiye aur ham jaise vahape int pe click kare to sare int ke types dikhne chahiye isliye
    return a+b

print(sum(5,7))



#match case :
#python 3.10 introduced the match statement , which is similar to the switch statement
#found in other programming languages.

def http_status(status):
    match status:
        case 200:
            return "OK"

        case 404:
            return "Not Found"

        case 500:
            return "Internal server Error"

        case _:
            return "Unknown status"   

print(http_status(5007))
print(http_status(500))
print(http_status(200))
print(http_status(404))



#Dictionary merge and update operator

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 3, 'c' : 4}

merged = dict1 | dict2
print(merged)


#you can now use multiple context managers in single with statement more cleanly using the paranthesised context manager


with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
