#Lists are mutable : we can make changes in existing list

fruits = ["Apple","Banana","Grapes","Orange","Kiwi",45,90.76,False,"akash"]
print(fruits[6])

fruits[0]="papaya"
print(fruits[0])

print(fruits[1:5])

fruits.append("Atirya")   #append means add karna
print(fruits)

l1 = [1,43,5,2,34,90,75]
#methods of list
#l1.sort()
#l1.reverse()
#l1.insert(2,234)
#print(l1.pop(3))
l1.remove(90)
print(l1)


#practice questions

# fruit =[]

# f1 =input("enter fruit here : ")
# fruit.append(f1)
# f2 = input("enter fruit here : ")
# fruit.append(f2)
# f3 =input("enter fruit here : ")
# fruit.append(f3)
# f4 = input("enter fruit here : ")
# fruit.append(f4)
# f5 = input("enter fruit here : ")
# fruit.append(f5)
# f6 = input("enter fruit here : ")
# fruit.append(f6)
# f7 = input("enter fruit here : ")
# fruit.append(f7)

# print(fruit)

# #q)2

# marks =[]

# f1 = int(input("enter marks here : "))
# marks.append(f1)
# f2 = int(input("enter marks here : "))
# marks.append(f2)
# f3 = int(input("enter marks here : "))
# marks.append(f3)
# f4 = int(input("enter marks here : "))
# marks.append(f4)
# f5 = int(input("enter marks here : "))
# marks.append(f5)
# f6 = int(input("enter marks here : "))
# marks.append(f6)

# marks.sort()

# print(marks)

#q)3

# a=(34,123,"Harry")
# a[2]="larry"         #it gives error because tupple elements cannot be changed 


#q)4

l = [7,3,6,1]
print(sum(l))

#q)5

n = (7,0,8,0,0,9)

b=n.count(0)    #it counts how many 0 in a tupple
print(b)
