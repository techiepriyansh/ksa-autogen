import os, sys
from distutils.dir_util import copy_tree

from treeaddergen import TreeAdderGen
from testbenchgen import TestBenchGen

algoFuncs = {}

def readConfig(pathToBinary):
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


def copyStaticFiles(pathToBinary):
  staticPath = os.path.join(pathToBinary, "static")
  copy_tree(staticPath, os.getcwd())


def main():
  pathToBinary = os.path.dirname(sys.executable) # when building the executable
  # pathToBinary = os.path.join(os.path.dirname(__file__), "..") # when running as a python script
  readConfig(pathToBinary)

  adderName = sys.argv[1]
  adderAlgoFuncName = f"{adderName}_algo"

  if not adderAlgoFuncName in algoFuncs.keys():
    print(f"Could not find {adderName} in any of the config files")
    sys.exit(1)

  N = int(sys.argv[2])
  k = len(bin(N-1)[2:])

  moduleName = f"{adderName}_{2**k}b"

  print("Writing static files black_cell.v and grey_cell.v")
  copyStaticFiles(pathToBinary)

  print(f"Writing adder design module {moduleName}.v")
  with open(f"{moduleName}.v", "w+") as designModuleFile:
    adder = TreeAdderGen(k, moduleName, algoFuncs[adderAlgoFuncName], designModuleFile)
    adder.generate()

  print(f"Writing test bench for the adder {moduleName}_tb.v")
  with open(f"{moduleName}_tb.v", "w+") as testBenchFile:
    testBench = TestBenchGen(k, moduleName, testBenchFile)
    testBench.generate()

  print("Done!")


if __name__ == "__main__":
  main()
