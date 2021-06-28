def sa_algo(k, merge):
  for i in range(1, k+1):
    for j in range(2**(k-i)):
      for l in range(j*2**i + 2**(i-1), (j+1)*2**i):
        merge(l, j*2**i + 2**(i-1), j*2**i)
