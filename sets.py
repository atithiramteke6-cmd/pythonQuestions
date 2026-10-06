#set is a collection of non-repetive elements
#elements order is mot maintained in a set while print a set and cannot access element by index
#all the elements of sets are  immutable and hashable


s = {1,5,7}
print(type(s))

e = set()   #empty set (don't use s = {} as it will create an empty dictionary)
print(type(e))


a = {1,65,87,90,1,1,1}  #(it prints 1 as one time because sets have only not-repetive elements)
print(a)         # elements order is mot maintained in a set while print a set and cannot access element by index

b={1,65,87,78,76,76,"Apple"}
print(b, type(b))

#methods of set
b.add(645)
print(b)


#operations on sets 
print(len(b))

b.remove(1)
print(b, type(b))

b.clear()
print(b)

#union and intersection in set

s1 = {1,34,8,7}
s2={7,3,1,87}
print(s1.union(s2))   #merge both the sets

print(s1.intersection(s2))  #only returns common value i  both the sets

print(s1-s2)   #cut the values which are persent in both sets and returns set s1



#practice questions

#Q)1

# d = {
#     "sambhalake" : "safely",
#     "Nadi" : "river",
#     "madat" : "help"
# }

# word = input("enter the words you want meaning of : ")
# print(d[word])

# #Q)2

# c = set()
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))
# n = input("enter no. : ")
# c.add(int(n))

# print(c)


#Q)3

r = set()
r.add(18)
r.add("18")

print(r)      
#we can add in a set 18 as int and 18 as string value

#Q)4

f=set()
f.add(20)
f.add(12.98)
f.add('34')
print(len(f))

#Q)5

h = {}  #its a empty dictionary
print(type(h))

#Q)6

# dict = {}

# name = input("enter Friends name: ")
# lang= input("enter their favourite language name : ")
# dict.update({name: lang})

# name = input("enter Friends name: ")
# lang= input("enter their favourite language name : ")
# dict.update({name: lang})

# name = input("enter Friends name: ")
# lang= input("enter their favourite language name : ")
# dict.update({name: lang})

# name = input("enter Friends name: ")
# lang= input("enter their favourite language name : ")
# dict.update({name: lang})

# print(dict)

#if the name is same in the above program and language is diffrent so it update the value of sane name friend
#example : ati : c and ati : js  so it update the value of ati from c to js means lastly it prints ati : js

#Q)7

p={8,23,"Ati",[1,3]}  #we cannot add list into the set
print(type(p))