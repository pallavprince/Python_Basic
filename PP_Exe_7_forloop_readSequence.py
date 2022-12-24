#Write a program using a for loop that loops over a sequence. What is the sequence?

"""sequence where we store multiple items or elements and we can iterate the items using loop"""
''' Example of sequence: List, set, dictionary, tuple, Array, string etc.'''


''' In this exercise we will create a list of 10 elements and then we will print each elements using for loop'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#we use here len(L) this means i value go from 0 to 10 i.e. size of list L
for i in range (len(L)):
    print(L[i])
