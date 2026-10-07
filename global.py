#global variable : jo ham fuction ke andar or bahar bhi chala sakte hai.

a = 89

def fun():
    #global a   #global keyword change the value of global variable to lacal variable value
    a = 3    #local variable
    print(a)

fun()
print(a)