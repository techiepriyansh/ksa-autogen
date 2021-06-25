from treeaddergen import TreeAdderGen
from testbenchgen import TestBenchGen

k = 4
moduleName = f"ksa_{2**k}b"

def ksa_algo(k, merge):
  for j in range(1, k+1):
    for i in range(2**(j-1), 2**k):
      merge(i, i+1-2**(j-1), max(i+1-2**j, 0))

ksa = TreeAdderGen(k, moduleName, ksa_algo)
ksa_tb = TestBenchGen(k, moduleName)

ksa.generate()
print("")
ksa_tb.generate()
