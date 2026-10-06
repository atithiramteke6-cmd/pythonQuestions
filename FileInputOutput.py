'''
RAM : the Random Access Memory is volatile and its contents are lost once a program
terminates in order to persist the data forever. we use files.

A file is data stored in a storage device . A python program can talk to the file by 
reading content from it and writing content to it.

computer program ---write---->   File
written in python <--read---

RAM = volatile
HDD=Non volatile

*types of files :
1)text files(.txt, .c etc)   ---(like open on vs code)
2)binary files(.jpg, .dat, etc)

python has a lots of functions to reading,updating and deleting files

'''

#opening or reading a file

# f = open("file.txt")
# data = f.read()
# print (data)
# f.close()


# #writing a file

# str = "Atithi, you are Amazing"
# f = open("my_file.txt","w")  #"w" means in write mode
# f.write(str)
# f.close()


#file functions

#f = open("file.txt")
# lines = f.readlines()       #redlines() function return a list
# print(lines,type(lines))


# readline() function tak tak chalta rehta hai jab tak use empty string na mil jaye
#example:
# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# line5 = f.readline()
# print(line5=="")

#we can write this logic into the loop also to reduce the no.of lines

# line = f.readline()
# while(line!= ""):
#       print(line)
#       line = f.readline()

# f.close()


#apending function
#means jitni bar ham ye program run kare utni bar ye "str" vali line "my_file.txt" file me add hogi.
# str = "Atithi, you are Amazing"
# f = open("my_file.txt","a")  
# f.write(str)
# f.close()



#with statement: using this with statement we dont have to need to write f.close() file automatically get close.

with open("file.txt") as f:
    print(f.read())




 