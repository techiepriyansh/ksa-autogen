import sys

from treeaddergen import TreeAdderGen
from testbenchgen import TestBenchGen

N = int(sys.argv[1])
k = len(bin(N-1)[2:])

moduleName = f"ksa_{2**k}b"

def ksa_algo(k, merge):
  for j in range(1, k+1):
    for i in range(2**(j-1), 2**k):
      merge(i, i+1-2**(j-1), max(i+1-2**j, 0))

with open(f"{moduleName}.v", "w+") as designModuleFile:
  ksa = TreeAdderGen(k, moduleName, ksa_algo, designModuleFile)
  ksa.generate()

with open(f"{moduleName}_tb.v", "w+") as testBenchFile:
  ksa_tb = TestBenchGen(k, moduleName, testBenchFile)
  ksa_tb.generate()


