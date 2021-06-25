import sys
import re

from io import StringIO
from modulegen import ModuleGen

class TreeAdderGen(ModuleGen):

  def __init__(self, k, moduleName, algo):
    super().__init__(moduleName)
    self.k = k
    self.algo = algo

    self.cnt = 0
    self.buffer = StringIO()


  def writeModule(self):
    super().writeModule("a, b, c_in, sum, c_out")


  def redirectToBuffer(self):
    sys.stdout = self.buffer


  def concatBuffer(self):
    print(self.buffer.getvalue(), end='')


  def restoreStdout(self):
    sys.stdout = sys.__stdout__


  def writeInput(self):
    print(f"input [{2**self.k}:1] a, b;")
    print(f"input c_in;\n")


  def writeOutput(self):
    print(f"output [{2**self.k}:1] sum;");
    print(f"output c_out;\n")


  def writeWiresWithPattern(self, pattern, size=''):
    txt = self.buffer.getvalue()
    wireRegex = re.compile(pattern)

    matches = wireRegex.findall(txt)
    wires = set()
    for match in matches:
      wire = match.replace('(', '').replace(')', '').replace(',', '').replace('[', '')
      wires.add(wire)

    print("wire ", end="")
    if size: print(f"{size} ", end="")
    print(f"{', '.join(sorted(list(wires)))};")


  def writeBaseCasePG(self):
    print("assign pg_0_0 = {1'b0, c_in};")
    print("assign g_0_0 = c_in;\n")


  def writeWires(self):
    pgWirePattern = r'\(?pg_[0-9]+_[0-9]+[,\)\[]?'
    gWirePattern = r'\b\(?g_[0-9]+_[0-9]+[,\)\[]?'

    self.writeWiresWithPattern(pgWirePattern, '[1:0]')
    self.writeWiresWithPattern(gWirePattern)
    print("wire c_out_tmp;")
    print("")


  def writeSingleBitPG(self):
    self.writeHeadingComment("Single Bit Propagates and Generates")

    n = 2**self.k

    self.writeComment("Single Bit Propagates")
    for i in range(1, n+1):
      print(f"xor(pg_{i}_{i}[1], a[{i}], b[{i}]);")
    print("")

    self.writeComment("Single Bit Generates")
    for i in range(1, n+1):
      print(f"and(pg_{i}_{i}[0], a[{i}], b[{i}]);")
    print("")


  def writeBlackCell(self, i, k, j):
    print(f"black_cell cell{self.cnt}(pg_{i}_{k}, pg_{k-1}_{j}, pg_{i}_{j});")
    self.cnt += 1


  def writeGreyCell(self, i, k, j):
    print(f"grey_cell cell{self.cnt}(pg_{i}_{k}, g_{k-1}_{j}, g_{i}_{j});")
    self.cnt += 1


  def merge(self, i, k, j):
    if j == 0: self.writeGreyCell(i, k, j)
    else: self.writeBlackCell(i, k, j)


  def writePGCombineLogic(self):
    self.writeHeadingComment("PG Combination Logic")
    self.algo(self.k, self.merge)
    print("")


  def writeSumAndCarryOut(self):
    self.writeHeadingComment("Sum and Carry Out")

    n = 2**self.k

    self.writeComment("Sum")
    for i in range(1, n+1):
      print(f"xor(sum[{i}], pg_{i}_{i}[1], g_{i-1}_0);")
    print("")

    self.writeComment("Carry Out")
    print(f"and(c_out_tmp, pg_{n}_{n}[1], g_{n-1}_0);")
    print(f"or(c_out, c_out_tmp, pg_{n}_{n}[0]);")
    print("")


  def generate(self):
    self.writeModule()
    self.writeInput()
    self.writeOutput()

    self.redirectToBuffer()
    self.writeSingleBitPG()
    self.writePGCombineLogic()
    self.restoreStdout()

    self.writeWires()
    self.writeBaseCasePG()
    self.concatBuffer()

    self.writeSumAndCarryOut()
    self.writeEndmodule()
