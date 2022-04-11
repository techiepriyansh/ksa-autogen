# TreeAdderAutoGen
Autogenerate verilog code for arbitrary parallel prefix adders

## Run - GUI
 * Clone/Download the repository
 * Run the executable `trag.exe` present in `dist/gui/`
 * Choose the `Project Location`, `Adder Type`, `Size` and click on the `Generate Tree Adder` button
 
   ![trag_example](https://user-images.githubusercontent.com/26199781/162727986-acf9a198-0d3d-4faf-a255-ab45b716b2fc.png)
 
 * The resulting files will be written to the chosen project location
    
    ![trag_example2](https://user-images.githubusercontent.com/26199781/162728665-f47fe99c-db13-4cfa-8a87-5bb852f497ea.png)
    
    ![trag_example3](https://user-images.githubusercontent.com/26199781/162728381-22ae68be-d957-4421-aed7-f272ba44b05a.png)

## Run - CLI
CLI usage and how to add custom adders is described [here](https://github.com/techiepriyansh/ksa-autogen/blob/main/dist/cli/README.md)

## (Re)Build from source
 * Clone the repository
 * Make sure you have `python3.8+` installed
 * Install the only pip requirement: `pip install Eel==0.12.4`
 * Execute
   * `make.bat clean` to cleanup files from previous builds 
   * `make.bat build` to build both the CLI and GUI tools
 * You can also selectively `build` / `clean` the CLI tool or the GUI tool by specifying `cli` or `gui` after the `make.bat build` and `make.bat clean` commands

## API reference
The class methods and functions are documented [here](https://github.com/techiepriyansh/ksa-autogen/tree/main/docs)
