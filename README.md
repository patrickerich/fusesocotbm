# fusesocotbm
Repo for checking added modelsim/questa flow support in fusesoc+cocotb

This repo contains a simple test setup for running a cocotb test with fusesoc.
The same sample cocotb test can be run with:
- icarus verilog
- verilator
- questa/modelsim

## Developed using
- AlmaLinux release 9.5 (Teal Serval)
- python 3.12
- gcc-toolset-13
- custom edalize fork with flow support for questa/modelsim

## Usage

Depending on your environment check if you need to modify the `sourceme.sh` script
(for instance if you want to change the python version, etc)

```bash
git clone https://github.com/patrickerich/fusesocotbm.git
cd fusesocotbm
source sourceme.sh
```

### Running the test

```bash
fusesoc run --target=sim_icarus fcm    # For running with Icarus verilog
fusesoc run --target=sim_verilator fcm # For running with Verilator
fusesoc run --target=sim_questa fcm    # For running with Questa/ModelSim
```
