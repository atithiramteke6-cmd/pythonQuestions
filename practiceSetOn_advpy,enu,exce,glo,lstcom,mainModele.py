#Q1) write a code to open tree files 1.txt, 2.txt and 3.txt if any three files are not present
#a message without axiting the program must be printed prompting the same.

try:
    with open("1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:     #this 2.txt is present so it print the content of 2.txt
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

print("Thankyou")



#Q2) write a code to print third , fifth, and seventh element from a list using enumerate function.

l = [23,45,12,1,23,78,90,54,98,34]

for i,item in enumerate(l):
    if i ==2 or i==4 or i==6:   #it prints item 3rd,5th and 7th so the index of 3rd element is 2 and index of 5th element is 4 likewise
        print(item)


#Q3) write a clist comprehensions to print a list which contains the multiplication table of a user entered number 

n = int(input("enter a number : "))
table = [n*i for i in range(1,11)]
print(table)


#Q4) write a program to display a/b where a and b are integers . if b = 0,display infinite by handeling the 'ZeroDivisionError'.

try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")


#Q5)   store the multiplication tables generated in problem 3 in a file named Tables.txt

n = int(input("enter a number : "))
table = [n*i for i in range(1,11)]
print(table)

with open("table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")