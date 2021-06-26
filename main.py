import os
import sys
import pathlib

from treeaddergen import TreeAdderGen
from testbenchgen import TestBenchGen

algoFuncs = {}

def readConfig():
  pathToBinary = pathlib.Path(__file__).parent.resolve()
  configPath = os.path.join(pathToBinary, "config")

  configFiles = []
  for (dirpath, dirnames, filenames) in os.walk(configPath):
    configFiles.extend(filenames)
    break

  for configFile in configFiles:
    with open(os.path.join(configPath, configFile), "r") as f:
      exec(f.read())

  for k,v in locals().items():
    if 'algo' in k: algoFuncs[k] = v


def main():
  readConfig()

  adderName = sys.argv[1]
  adderAlgoFuncName = f"{adderName}_algo"

  if not adderAlgoFuncName in algoFuncs.keys():
    print(f"Could not find {adderName} in any of the config files")
    sys.exit(1)

  N = int(sys.argv[2])
  k = len(bin(N-1)[2:])

  moduleName = f"{adderName}_{2**k}b"

  with open(f"{moduleName}.v", "w+") as designModuleFile:
    adder = TreeAdderGen(k, moduleName, algoFuncs[adderAlgoFuncName], designModuleFile)
    adder.generate()

  with open(f"{moduleName}_tb.v", "w+") as testBenchFile:
    testBench = TestBenchGen(k, moduleName, testBenchFile)
    testBench.generate()


if __name__ == "__main__":
  main()
