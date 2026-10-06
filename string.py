name = "atithi"
nameShort = name[0:3]   #start from index 0 and end with 2nd index(excluding 3)
print(nameShort)

character1 = name[1]

print(character1)

#picchese string ko read kiye to negative starting hoti hai (start from -1...)

print(name[-4:-1])
#convert -ve integer into +ve integer
print(name[1:4])

print(name[:4])  #starting from 0 [0:4]

print(name[1:])  #blank space means (len-1)   [1:6]

#slicing with skip value

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:11:3])          #it starts from 1 to 11 and that string ko 3 se aage badhaye 

#functions of string

print(len(name))
print(name.endswith("thi"))
print(name.endswith("arya"))
print(name.startswith("ati"))
print(name.startswith("Ati"))
print(name.capitalize())
print(name.find("thi"))
print(name.replace("thi","rya"))  #replace all occurances

#escape sequence character

# \n - for adding new line
# \t - tab(more space)
# \'  \'  - single quote into single quate
#\"  \" - for use qutation into quatation


name =input("enter your name : ")
print(f"Good Afternoon , {name} ")     #f string se direct ham name print kar sakte hai with good afternoon without concatenation and all

letter = '''Dear <|Name|> , 
you are selected!
<|date|>'''

print(letter.replace("<|Name|>","Atithi").replace("<|date|>","13 April 2028"))  #chaining of .replace fuction

#detect doble space
a="atithi is a  good girl  "
print(a.find("  "))

#replace double space with single space

b="atithi is a  good girl  "
print(b.replace("  "," "))   #string are immutable which means that you cannot change them by running functions on them.


letter = "Dear Atirya,\n\tthis python course is nice .\nThanks!"
print(letter)