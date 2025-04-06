import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock


class StimulusGenerator:
    def __init__(self, dut, clk, signal, values, delay_cycles=0):
        self.dut = dut
        self.clk = clk
        self.signal = signal
        self.values = values
        self.delay_cycles = delay_cycles

    async def run(self):
        for _ in range(self.delay_cycles):
            await RisingEdge(self.clk)
        for val in self.values:
            await RisingEdge(self.clk)
            self.signal.value = val
            self.dut._log.info(f"Driving input_signal = {val}")


@cocotb.test()
async def test_fcm(dut):
    # cocotb.start_soon(Clock(dut.clk, 10, units="ns").start()) 
    # Updated in cocotb 2.0.0 untits -> unit
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start()) 

    dut.reset.value = 1
    for _ in range(2):
        await RisingEdge(dut.clk)
    dut.reset.value = 0

    stim = StimulusGenerator(dut, dut.clk, dut.input_signal, [1, 2, 3, 4], delay_cycles=1)
    await stim.run()

