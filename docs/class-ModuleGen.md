# Class: ModuleGen

### Purpose: 
To help generating verilog files by providing utility functions

### Constructor:
- ##### Syntax: `ModuleGen(self, moduleName, outStream)`
- Initialization of the required variables

### redirectToOutstream:
- ##### Syntax: `redirectToBuffer(self)`
- Sets `stdout` stream to `outStream`

### restoreStdout:
- ##### Syntax: `restoreStdout(self)`
- Sets `stdout` back to default

### writeModule:
- ##### Syntax: `writeModule(self)`
- Prints the module declaration statement

### writeEndmodule:
- ##### Syntax: `writeEndmodule(self)`
- Prints the endmodule statement

### writeHeadingComment:
- ##### Syntax: `writeHeadingComment(self, comment)`
- Prints a comment in the heading format

### writeComment:
- ##### Syntax: `writeComment(self, comment)`
- Prints a comment
