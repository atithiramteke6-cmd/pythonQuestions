# dictionary is a key - value pair
#dictionary is mutable
#cannot contain duplicate key
#it is unorders

d = {}   #empty dictionary

marks = {
    "Atithi" : 100,
    "Atirya" : 89,
    "Arya" : 80,
    13 : "Ishu"
}

print(len(marks))  #it prints 4 because this dictionary has 4 key-value pair
print(marks, type(marks))
print(marks["Atirya"])


#dict methods
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Arya" : 85 , "Shamru" : 84})
print(marks)
print(marks.get("shivika"))
print(marks.get("Arya2"))     #prints None
print(marks["Arya2"])      #returns an error

#others methods also we discover  in chatgpt

