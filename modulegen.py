class ModuleGen:

  def __init__(self, moduleName):
    self.moduleName = moduleName


  def writeModule(self, ports=""):
    print(f"module {self.moduleName}", end="")
    if ports: print(f"({ports})", end="")
    print(f";\n")


  def writeEndmodule(self):
    print(f"endmodule")


  def writeHeadingComment(self, comment):
    print(f"/*-----{len(comment) * '-'}-----")
    print(f"  |    {comment}    |")
    print(f"  -----{len(comment) * '-'}-----*/")
    print("")


  def writeComment(self, comment):
    print(f"// {comment}")
