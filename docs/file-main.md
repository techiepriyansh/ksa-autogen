# File: main.py

### Purpose: 
- To read the config files and the input from user
- To instantiate TreeAdderGen and TestBenchGen by passing in the user inputs
- To invoke functions which generate the main verilog code and the test bench and store them in respective files in the current working directory

### readConfig:
- ##### Syntax: `readConfig(pathToBinary)`
- Reads the config files present in the config folder which is present in the directory of the executable

### copyStaticFiles:
- ##### Syntax: `copyStaticFiles(pathToBinary)`
- Copies the static files (black_cell.v and grey_cell.v) present in the static folder in the directory of the executable to the current working directory

### main:
- ##### Syntax: `main()`
- Reads input from the user and instantiates TreeAdderGen and TestBenchGen by passing in the user inputs
- Invokes functions which generate the main verilog code and the test bench and stores them in respective files in the current working directory
