# Class: ModuleGen

### Purpose: 
To help generating verilog files by providing utility functions

### Constructor:
- ##### Syntax: `ModuleGen(moduleName, outStream)`
- Initializes the required variables

### redirectToOutstream:
- ##### Syntax: `redirectToBuffer()`
- Sets `stdout` stream to `outStream`

### restoreStdout:
- ##### Syntax: `restoreStdout()`
- Sets `stdout` back to default

### writeModule:
- ##### Syntax: `writeModule()`
- Prints the module declaration statement

### writeEndmodule:
- ##### Syntax: `writeEndmodule()`
- Prints the endmodule statement

### writeHeadingComment:
- ##### Syntax: `writeHeadingComment(comment)`
- Prints a comment in the heading format

### writeComment:
- ##### Syntax: `writeComment(comment)`
- Prints a comment
