# Class: TestBenchGen

### Purpose: 
To print test bench code for a given value of `k`, where:
- `k` is the smallest integer such that 2<sup>k</sup> is greater than or equal to the given input `N`

### Constructor:
- ##### Syntax: `TestBenchGen(k, designModuleName, outStream)`
- Makes parent constructor call and initializes the required variables

### writeInput:
- ##### Syntax: `writeInput()`
- Prints declarations for input registers

### writeOutput:
- ##### Syntax: `writeOutput()`
- Prints declarations for output wires

### writeVariables:
- ##### Syntax: `writeVariables()`
- Prints declarations for variables

### writeInstance:
- ##### Syntax: `writeInstance()`
- Prints tree adder instantiation statement

### writeInitialize:
- ##### Syntax: `writeInitialize()`
- Prints statements to initialize input registers

### writeDisplay:
- ##### Syntax: `writeDisplay()`
- Prints statements to display the results of the adder

### writeMain:
- ##### Syntax: `writeMain()`
- Prints statements to test the adder for random values of the input registers

### generate:
- ##### Syntax: `generate()`
- Invokes functions step by step in order to generate the required test bench file
