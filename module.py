# if__name__ == "__main__" in python

'''__name__ evaluates to the name of the module in python from where the program is ran.'''


def myFunc():
    print("Hello World!")

if __name__ == "__main__":       #jis file se import kar rahe hai uska name hota hai
    #if this code is directly executed by running the file its present in
    print("we are directly running this code")
    myFunc()
    print(__name__)