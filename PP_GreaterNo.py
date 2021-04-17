### if ; elif ; else Condition
### This example code is to find which input number is greater

a=int(input("Enter a 1st No.: "))
b=int(input('Enter 2nd No.: '))

if a==b:
    print('your 1st No. '+str(a)+ ' is equal to your 2nd No. '+str(b))
elif a>b:
    print(str (a)+' is greater than '+str(b))
else:
    print(str(b)+' is greater than '+str(a))
