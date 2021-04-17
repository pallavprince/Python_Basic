### This is the python code to find tne total No. of digits in a given Number

def digit_find(x):
    (q,d) = (1,0)
    while q <= x:
        (q,d) = (q*10,d+1)
    return(d)
