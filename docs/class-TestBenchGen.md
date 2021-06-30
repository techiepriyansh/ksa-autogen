# Class: TestBenchGen

### Purpose: 
To print test bench code for a given value of `k`, where:
- `k` is the smallest power of 2 greater than or equal to the given input `N`

### Constructor:
- ##### Syntax: `TestBenchGen(self, k, designModuleName, outStream)`
- Parent contructor call and initialization of the required variables

### writeInput:
- ##### Syntax: `writeInput(self)`
- Prints declarations for input registers

### writeOutput:
- ##### Syntax: `writeOutput(self)`
- Prints declarations for output wires

### writeVariables:
- ##### Syntax: `writeVariables(self)`
- Prints declarations for variables

### writeInstance:
- ##### Syntax: `writeInstance(self)`
- Print tree adder instantiation statement

### writeInitialize:
- ##### Syntax: `writeInitialize(self)`
- Print statements to initialize input registers

### writeDisplay:
- ##### Syntax: `writeDisplay(self)`
- Print statements to display the results of the adder

### writeMain:
- ##### Syntax: `writeMain(self)`
- Print statements to test the adder for random values of the input registers

### generate:
- ##### Syntax: `generate(self)`
- Call functions step by step in order to generate the required test bench file
