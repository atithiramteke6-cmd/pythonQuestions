#practice questions of if else elif

#Q)1
# a1=int(input("enter no. 1: "))
# a2=int(input("enter no. 2: "))
# a3=int(input("enter no. 3: "))
# a4=int(input("enter no. 4: "))

# if(a1 > a2 and a1 > a3 and a1 >a4):
#     print("greatest no. is a1 : ",a1)

# elif(a2 > a1 and a2 > a3 and a2 >a4):
#     print("greatest no. is a1 : ",a2)

# elif(a3 > a1 and a3 > a2 and a3 >a4):
#     print("greatest no. is a1 : ",a3)

# elif(a4 > a1 and a4 > a2 and a4 >a3):
#     print("greatest no. is a4 : ",a4)



#Q)2

# m1 = int(input("enter marks of sub 1 : "))
# m2 = int(input("enter marks of sub 2 : "))
# m3 = int(input("enter marks of sub 3 : "))

# #check for total
# total_percentage =(100* (m1+m2+m3)) / 300

# if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):   #har subjects me marks 33 ya 33 se jyada hona chahiye and total percentage 40 ya 40 se jyada hone chahiye
#     print("you are pass : ",total_percentage)

# else:
#     print("you are fail,try again next year! : ",total_percentage)


#Q)3 - checking spam or not

# p1 = "make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("enter your comment : \n")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is spam")

# else:
#     print("This comment is not spam")


#Q)4 - check user name contain less than 10 character

# username = input("enter username : ")

# if(len(username)<10):
#     print("your username contains less than 10 characters")
# else:
#     print("your username contains more than or equal to 10 characters")


#Q)5

# l = ["atithi","bhumi","atirya","dhanu"]

# name = input("enter your name : ")

# if(name in l):
#     print("your name is in the list")

# else:
#     print("name not in list")


#Q)6

# marks = int(input("enter your marks : "))

# if(marks<=100 and marks>=90):
#     grade= "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "F"


# print("your grade is : ",grade)


#Q)7  -  check post talking about atithi or not

post = input("Enter the post : ")

if("atithi" in post.lower()):
    print("This post is talking about Atithi")

else:
    print("This post is not talking about Atithi")





