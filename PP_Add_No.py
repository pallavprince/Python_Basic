###This is the concept of global variable and call that global variables in the defined function
### Eample code is for adding two numbers



global a, b, r
r=0
a=0
b=0
def mycalculator():
    global a, b, r
    a=int(input("Enter no.: "))
    b=int(input("Enter Second No.: "))

    r=(a+b)




mycalculator()
print("My result of summation= " + str(r))



