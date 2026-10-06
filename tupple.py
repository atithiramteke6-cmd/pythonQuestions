#tupples are immutable
a=(1,2,3,4,5,3,5,"rohan",97.9,True)
print(type(a))

b=(1,)   #only 1 element in a tupple
print(type(b))


#methods of tupple
print(a.count(5))        #5 exist 2 times in a tupple
print(a.index(97.9))     #it return index
print(a*3)       #repeat tupple 3 times
print(len(a))

#this below method use to check the element is present in tupple or not . if present it returns True and if not it returns False
print("rohan" in a)
print(True in a)
print(4657 in a)

#slicing in tupple
print(a[1:5])


