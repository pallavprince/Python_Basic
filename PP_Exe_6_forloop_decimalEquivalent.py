# Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, upto 1/10

'''Here we will use for loop to generate number 2, 3, 4, 5, 6, upto 10 and then will print value of 1/2, 1/3 so on...'''


# to go up to 10 we need to run loop upto 11 (n-1)
print("The Decimal value of:")
for i in range(2, 11):
    print(" 1/" + str(i) + " = " + str(1/i))
