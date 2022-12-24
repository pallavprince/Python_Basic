# Write a program to compute distance between two points taking input from the user. (Pythagorean 'Theorem)

''' we need point coordinate of two points let suppose P1 and P2.
then P1=(x1, y1) and P2= (x2, y2)

Distance D = sqroot((x2-x1)^2 + (y2-y1)^2) '''

x1 = input("Enter Point P1 x coordinate x1 = ")
y1 = input("Enter Point P1 y coordinate y1 = ")

x2 = input("Enter Point P2 x coordinate x2 = ")
y2 = input("Enter Point P2 y coordinate y2 = ")

print ("Point P1 = " + "(" + x1 + "," + y1 +")")
print ("Point P2 = " + "(" + x2 + "," + y2 +")")

# convert input value in integer
x1 = int (x1)
y1 = int (y1)
x2 = int (x2)
y2 = int (y2)

D = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)

print ("Distance between P1 and P2 = " +str (D))



