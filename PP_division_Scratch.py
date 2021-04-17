#this is code for find quotient of two no. in which dividend is greater than divisor.
#that mean this code give result as  m/n= ans  where ans in integer.
# in this code divisor is substracted fron dividend and number of times of substaction is counted.
''' The beauty of code is divide the number without using any predefine function'''

def find_quotient(m,n):
    ans = 0
    while (m >= n):
        (ans,m) = (ans+1,m-n) 
    return(ans)

