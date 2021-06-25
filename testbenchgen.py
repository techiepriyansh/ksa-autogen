import sys
import random

from modulegen import ModuleGen

class TestBenchGen(ModuleGen):

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
    print(f"real i;\n")


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
    print(f"  $monitor( \"a(%d) + b(%d) + c_in(%d) = c_out sum(%d %d)\", a, b, c_in, c_out, sum); \n")


  def writeMain(self):
    self.writeComment("Assigning random values to a and b")
    
    decrement = bin(random.randint(2**(2**(self.k-1)), 2**(2**self.k)))[2:]

    print(f"always @(a or b or c_in)")
    print(f"begin")
    print(f"  for (i={2**(self.k+1)}'b{'1'*(2**(self.k+1))}; i > 0; i = i - {len(decrement)}'b{decrement})")
    print(r"    #1 {a, b} = i;")
    print(f"    #10 $stop;")
    print(f"end \n")


  def generate(self):
    self.writeModule()
    self.writeInput()
    self.writeOutput()

    self.writeVariables()
    self.writeInstance()

    self.writeInitialize()
    self.writeDisplay()
    self.writeMain()

    self.writeEndmodule()
