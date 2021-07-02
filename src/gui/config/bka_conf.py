def bka_algo(k, merge):
  for i in range(1, k+1):
    for j in range(2**i-1, 2**k, 2**i):
      merge(j, j+1-2**(i-1), j+1-2**i)

  for i in range(1, k):
    for j in range(2*i-1):
      merge(2**k-1-2**(k-i-1) - j*(2**(k-i)), 2**k-2**(k-i) - j*2**(k-i), 0)
