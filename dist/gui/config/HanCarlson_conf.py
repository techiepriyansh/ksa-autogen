def HanCarlson_algo(k, merge):
  for i in range(1, 2**k, 2):
    merge(i, i, i-1)

  for i in range(2, k+1):
    for j in range(2**(i-1)+1, 2**k, 2):
      merge(j, j+1-2**(i-1), max(j+1-2**i, 0))

  for i in range(2, 2**k, 2):
    merge(i, i, 0)