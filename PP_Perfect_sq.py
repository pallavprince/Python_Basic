#this code is for find given no is perfect squere or not
# 
def is_sqr(n):
    f = 0
    j=0
    k=0
    for i in range(1,n+1):
      if n%i == 0:
        f = f + 1
        j=n/i
#        while i==j:               #this two lines we use for find the sq of no
#           return(j)
    return(f%2 == 1)
    
    

