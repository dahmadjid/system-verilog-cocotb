### SystemVerilog Vscode simulator setup with cocotb.
This worked in ubuntu 24.04

### Requirements
- python
- pip install cocotb
- sudo apt install verilator iverilog
- verible binaries from chipsalliance github releases
- veridian vscode extension from https://github.com/vivekmalneedi/veridian

### Run testbenches
- python test_runner.py
- in test_runner.py, you can use verilator or icarus by changing cocotb runner.
- icarus is interpreted which is nice for small projects.
