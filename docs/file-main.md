# File: main.py

### Purpose: 
- To read the config files and the input from user
- To instantiate TreeAdderGen and TestBenchGen by passing in the user inputs
- To invoke functions which generate the main verilog code and the test bench and store them in respective files

### readConfig:
- ##### Syntax: `readConfig(pathToBinary)`
- Reads the config files present in the path provided and stores their contents

### copyStaticFiles:
- ##### Syntax: `copyStaticFiles(pathToBinary)`
- Copies the static files of the project into the current working directory

### main:
- ##### Syntax: `main()`
- Reads input from the user and instantiates TreeAdderGen and TestBenchGen by passing in the user inputs
- Invokes functions which generate the main verilog code and the test bench and store them in respective files
