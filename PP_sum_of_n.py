
#sum of n natural no.
def sum_N(m):
    if m == 0:
      return(0)
    else:
      return(m+sum_N(m-1))

