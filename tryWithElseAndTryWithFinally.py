#try with  else : agar try vala block successfully run hua to direct else vala block chalega
#agar try vala block run nahi hua except vala block run hua to else block run nahi hoga.

# try:
#     a = int(input("enter  a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# else:
#     print("I am inside else")


#try with finally : finally vala block chalega hi chalega if agar ham try vala chalaye ya except vala

'''first way '''
# try:
#     a = int(input("enter  a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# finally:
#     print("I am inside finally")


'''second way : if we doesn't write finally it also run in both cases try or except'''
# try:
#     a = int(input("enter  a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# print("I am inside finally")



'''finally mainly use in function'''
def main():
    
    try:
        a = int(input("enter  a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside finally")    #if we write only this print("I am inside finally") as second way so ye nahi chalega fuction me 

main()