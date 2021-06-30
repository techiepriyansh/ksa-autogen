# Tree Adder Auto Generator
Generates N bit tree adder with the given algorithm

## Usage
`trag.exe <adder-name> N`

## Custom Adders
You can even provide a custom algorithm for PG (Propagate and Generate) combination by creating a config file in the `config` directory.
* Create a new file in the `config` directory (preferably named `<adder-name>_conf.py`)
* In that file define a python like function named `<adder-name>_algo` which takes two parameters `k` and `merge`. Here:
    * `k = ceil(log2(N))` 
    *  `merge` contains the reference to the `merge` function which is used to combine the PGs of two adjacent groups. `merge(i, k, j)` merges the PG of group i to k with that of group k-1 to j yielding the PG for group i to j.
* Using these two parameters, write the alogrithm in python syntax
* Use this algorithm to create an adder by executing `trag.exe <adder-name> N` where `<adder-name>` is the name of your custom defined adder
