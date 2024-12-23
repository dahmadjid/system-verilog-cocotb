import cocotb
from cocotb.handle import HierarchyObject
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test() # type: ignore
async def test(dut: HierarchyObject):
    dut.a = 1
    await Timer(1)
    print(dut.b)