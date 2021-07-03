def KoggeStone_algo(k, merge):
  for j in range(1, k+1):
    for i in range(2**(j-1), 2**k):
      merge(i, i+1-2**(j-1), max(i+1-2**j, 0))
