# Class: TreeAdderGen

### Purpose: 
To print main verilog code for a given value of `k` and a given function `algo`, where:
- `k` is the smallest integer such that 2<sup>k</sup> is greater than or equal to the given input `N`
- `algo` is the given function which instructs the combination logic of the adder

### Constructor:
- ##### Syntax: `TreeAdderGen(k, moduleName, algo, outStream)`
- Makes parent constructor call and initializes the required variables

### writeModule:
- ##### Syntax: `writeModule()`
- Prints the module declaration statement

### redirectToBuffer:
- ##### Syntax: `redirectToBuffer()`
- Sets `stdout` stream to `buffer`

### concatBuffer:
- ##### Syntax: `concatBuffer()`
- [TODO]

### writeInput:
- ##### Syntax: `writeInput()`
- Prints declarations for input ports

### writeOutput:
- ##### Syntax: `writeOutput()`
- Prints declarations for output ports

### writeWiresWithPattern:
- ##### Syntax: `writeWiresWithPattern(pattern, size)`
- Prints declarations for the required wires according to the `pattern` passed as regular expression

### writeBaseCasePG:
- ##### Syntax: `writeBaseCasePG()`
- Prints the base cases of `pg` and `g`

### writeWires:
- ##### Syntax: `writeWires()`
- Prints declarations for wires

### writeSingleBitPG:
- ##### Syntax: `writeSingleBitPG()`
- Prints gate-level statements to initialize single bit propagates and generates

### writeBlackCell:
- ##### Syntax: `writeBlackCell(i, k, j)`
- Prints black cell instantiation statement

### writeGreyCell:
- ##### Syntax: `writeGreyCell(i, k, j)`
- Prints grey cell instantiation statement

### merge:
- ##### Syntax: `merge(i, k, j)`
- [TODO]

### writePGCombineLogic:
- ##### Syntax: `writePGCombineLogic()`
- Prints statements which construct the PG combination logic using the `algo` function

### writeSumAndCarryOut:
- ##### Syntax: `writeSumAndCarryOut()`
- Prints final gate-level statements to assign values to the outputs, `sum` and `c_out`

### generate:
- ##### Syntax: `generate()`
- Invokes functions step by step in order to generate the required verilog file
