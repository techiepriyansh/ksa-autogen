# Class: TreeAdderGen

### Purpose: 
To print main verilog code for a given value of `k` and a given function `algo`, where:
- `k` is the smallest power of 2 greater than or equal to the given input `N`
- `algo` is a user defined function which instructs the combination logic of the adder.

### Constructor:
- ##### Syntax: `TreeAdderGen(self, k, moduleName, algo, outStream)`
- Parent contructor call and initialization of the required variables

### writeModule:
- ##### Syntax: `writeModule(self)`
- Prints the module declaration statement

### redirectToBuffer:
- ##### Syntax: `redirectToBuffer(self)`
- Sets `stdout` stream to `self.buffer`

### concatBuffer:
- ##### Syntax: `concatBuffer(self)`
- [TODO]

### writeInput:
- ##### Syntax: `writeInput(self)`
- Prints declarations for input ports

### writeOutput:
- ##### Syntax: `writeOutput(self)`
- Prints declarations for output ports

### writeWiresWithPattern:
- ##### Syntax: `writeWiresWithPattern(self, pattern, size)`
- Print declarations for the required wires according to the `pattern` passed as regular expression

### writeBaseCasePG:
- ##### Syntax: `writeBaseCasePG(self)`
- Print the base cases of `pg` and `g`

### writeWires:
- ##### Syntax: `writeWires(self)`
- Generates `pattern` for printing wire declarations and invokes `writeWiresWithPattern`

### writeSingleBitPG:
- ##### Syntax: `writeSingleBitPG(self)`
- Print gate-level statements to initialize single bit propagates and generates

### writeBlackCell:
- ##### Syntax: `writeBlackCell(self, i, k, j)`
- Print black cell instantiation statement

### writeGreyCell:
- ##### Syntax: `writeGreyCell(self, i, k, j)`
- Print grey cell instantiation statement

### merge:
- ##### Syntax: merge(self, i, k, j)
- [TODO]

### writePGCombineLogic:
- ##### Syntax: `writePGCombineLogic(self)`
- Print statements which construct the PG combination logic using the `algo` function

### writeSumAndCarryOut:
- ##### Syntax: `writeSumAndCarryOut(self)`
- Print final gate-level statements to assign values to the outputs, `sum` and `c_out`

### generate:
- ##### Syntax: `generate(self)`
- Call functions step by step in order to generate the required verilog file
