from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import BinaryResource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA

# A simple script (similar to the hello-world script from the stdlib tutorial)
# to test with different CPU models
# We will run a simple application with AtomicSimpleCPU, TimingSimpleCPU, and
# O3CPU using two different cache sizes

cache_hierarchy = PrivateL1CacheHierarchy(l1d_size="32KiB", l1i_size="32KiB")
memory = SingleChannelDDR3_1600("1GiB")

processor = SimpleProcessor(cpu_type=CPUTypes.O3, num_cores=1, isa=ISA.X86)

board = SimpleBoard(clk_freq="3GHz", processor=processor, memory=memory,
    cache_hierarchy=cache_hierarchy)

binary = BinaryResource("materials/using-gem5/05-cpu-models/IntMM/IntMM")
board.set_se_binary_workload(binary)

simulator = Simulator(board=board)
simulator.run()