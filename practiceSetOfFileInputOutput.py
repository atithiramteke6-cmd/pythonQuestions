#Q)1- write a code to read the text file from poem.txt and find the word twinkle present in content or not

# f = open("poem.txt")
# content = f.read()
# if("Twinkle" in content):
#     print("Twinkle is present in the content")

# else:
#     print("Twinkle is not present in content")
# f.close()


#Q2) the game function in a program lets a user play a game and returns the score as an integer.
#you need to read a file 'Hi-score.txt' which is either blank or contains the previous
#Hi-score.you need to write a program to update the Hi-score whenever the game() function breaks the Hi- score.

# import random
# def game():
#     print("You are playing the game...")
#     score = random.randint(1,76)
#     #fetch the hiscore
#     with open ("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore !=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print(f"Your score: {score}")
#     if(score>hiscore):
#         #write thi hiscore to the file
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score

# game()



#Q3) write a code to generate multiplication table from 2 to 20 and write it to the 
#different files.plsce these files in s folder for a 13-year old.



# def generateTable(n):
#     table = ""
#     for i in range (1,11):
#         table +=f"{n} * {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)


# for i in range(2,21):
#     generateTable(i)


#Q4) a file contains a word "Donkey" multiple times . you need to write a program which 
#replace this word with ###### by updating a same file.
 

# word = "Donkey"

# with open ("file_04.txt","r") as f:
#     content = f.read()

# contentNew = content.replace(word, "######")

# with open("file_04.txt","w") as f:
#     f.write(contentNew)



#Q5) Repeat the program 4 for a list of such words to be censored.


# words = ["Donkey","bad","ganda"]

# with open ("file_04.txt","r") as f:
#     content = f.read()

# for word in words :
#     content = content.replace(word, "#" * len(word))

# with open("file_04.txt","w") as f:
#     f.write(content)


#Q6) write a program to mine a log file and find out whether it contains 'python'.

# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("Yes,python is present")

# else:
#     print("python is not present")



#Q7) write a program to find out the line number where the python is present from que 6

# with open("log.txt") as f:
#     lines = f.readlines()
# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"Yes,python is present.line no. : {lineno}")
#         break
#     lineno += 1

# else:
#     print("python is not present")



#Q8)  write a program to make a copy of a text file"this.txt"

# with open("this.txt") as f:
#     content = f.read()

# with open("this_copy.txt","w") as f:
#     f.write(content)


#Q9) write a program to find out whether a file is identical and matches the content of another file

# with open("this.txt") as f:
#     content1 = f.read()

# with open("this_copy.txt") as f:
#     content2 = f.read()

# if(content1==content2):
#     print("yes , these files are identical")

# else:
#     print("no, these files are not identical")





#Q10) write a program to wipe out the content of a file using python

# with open("this_copy.txt","w") as f:
#     f.write("")




#Q11)  write a python program to rename a file to "renamed_by_python.txt"


with open("old.txt") as f:
     content = f.read()

with open("renamed_by_python.txt","w") as f:
     f.write(content)
