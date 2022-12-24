# Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero.
''' Here we use while loop and we start dicresing the loop size for countdown process'''


N = int(input("Enter a number to show count down= "))

print("Count down start from "+ str(N))

while N>0:
    N=N-1
    print (N)
    
