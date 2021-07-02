import os, sys, eel

import dialogs
import utils

from treeaddergen import TreeAdderGen
from testbenchgen import TestBenchGen

eel.init('views')

algoFuncs = {}
pathToBinary = ''

@eel.expose
def initialize():
  utils.readConfig(pathToBinary, algoFuncs)

  return list(map(lambda k: k[:-5], algoFuncs.keys()))


@eel.expose
def ask_folder():
  return dialogs.ask_folder()


@eel.expose
def generateVerilog(projectLocation, adderName, N):
  k = len(bin(N-1)[2:])

  moduleName = f"{adderName}_{2**k}b"
  adderAlgoFuncName = f"{adderName}_algo"

  eel.putMessageInOutput("Writing static files black_cell.v and grey_cell.v")()
  utils.copyStaticFiles(pathToBinary, projectLocation)

  eel.putMessageInOutput(f"Writing adder design module {moduleName}.v")()
  with open(os.path.join(projectLocation, f"{moduleName}.v"), "w+") as designModuleFile:
    adder = TreeAdderGen(k, moduleName, algoFuncs[adderAlgoFuncName], designModuleFile)
    adder.generate()

  eel.putMessageInOutput(f"Writing test bench for the adder {moduleName}_tb.v")()
  with open(os.path.join(projectLocation, f"{moduleName}_tb.v"), "w+") as testBenchFile:
    testBench = TestBenchGen(k, moduleName, testBenchFile)
    testBench.generate()

  eel.putMessageInOutput("Done!")()


def start():
  eel.start('index.html', size=(650, 550), port=1337)


if __name__ == "__main__":
  pathToBinary = os.path.dirname(sys.executable) # when building the executable
  # pathToBinary = os.path.join(os.path.dirname(__file__), "..") # when running as a python script

  start()