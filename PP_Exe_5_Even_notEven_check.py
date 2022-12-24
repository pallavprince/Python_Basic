#Write a Program for checking whether the given number is an even number or not.

N = int(input("Enter any number to test whether it is even or not= "))

#condition check for Even here we use mode oprator by dividing 2 if reminder 0 then it is even
if (N % 2) == 0:
    print ("Given number is Even")

else:
    print ("Given number is Not Even")
