#### Here is concept of user defined function inside the function and call one function in other function
### Eample code is to join two strings

def PP_myfirstfunc():
    def PP_myfirst():
        print("hi")
    PP_myfirst()
    name=str(input("Type your Name: "))
    print("Hello "+name+"!")
    print("This is your first user defined function")
    
PP_myfirstfunc()

