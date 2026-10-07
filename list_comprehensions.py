'''list comprehensions is the elegant way to create lists based on existing lists'''

myList = [1,2,5,3,9,5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

'''this can be easy using list comprehensions'''

squaredList = [i*i for i in myList]

print(squaredList)