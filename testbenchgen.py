import sys
import random

from modulegen import ModuleGen

class TestBenchGen(ModuleGen):

  numTests = 100

  def __init__(self, k, designModuleName, outStream=sys.__stdout__):
    super().__init__(f"{designModuleName}_tb", outStream)

    self.designModuleName = designModuleName
    self.k = k


  def writeEndmodule(self):
    print(f"endmodule")


  def writeInput(self):
    print(f"reg [{2 ** self.k}:1] a, b;")
    print(f"reg c_in;\n")


  def writeOutput(self):
    print(f"wire [{2 ** self.k}:1] sum;")
    print(f"wire c_out;\n")


  def writeVariables(self):
    print(f"integer i;\n")


  def writeHeadingComment(self, comment):
    print(f"/*-----{len(comment) * '-'}-----")
    print(f"  |    {comment}    |")
    print(f"  -----{len(comment) * '-'}-----*/")
    print("")
    pass


  def writeComment(self, comment):
    print(f"// {comment}")


  def writeInstance(self):
    print(f"{self.designModuleName} inst(.a(a), .b(b), .c_in(c_in), .sum(sum), .c_out(c_out));\n")


  def writeInitialize(self):
    print(f"initial begin")
    print(f"  a=0;")
    print(f"  b=0;")
    print(f"  c_in=0;")
    print(f"end \n")


  def writeDisplay(self):
    print(f"initial")
    print(f"  $monitor( \"a(%d) + b(%d) + c_in(%b) = c_out sum(%b %d)\", a, b, c_in, c_out, sum); \n")


  def writeMain(self):
    self.writeComment("Assigning random values to a and b")
    
    randBlocks32b = []
    for i in range(2**max(0, self.k - 4)):
      randBlocks32b.append("$random")
    randBlocks32bString = "{" + ", ".join(randBlocks32b) + "}"

    print(f"initial")
    print(f"begin")
    print(f"  for (i = 0; i < {self.numTests}; i = i + 1)")
    print(r"    #1 {a, b} = " + randBlocks32bString + ";")
    print(f"  #10 $stop;")
    print(f"end \n")


  def generate(self):
    self.redirectToOutStream()

    self.writeModule()
    self.writeInput()
    self.writeOutput()

    self.writeVariables()
    self.writeInstance()

    self.writeInitialize()
    self.writeDisplay()
    self.writeMain()

    self.writeEndmodule()

    self.restoreStdout()
