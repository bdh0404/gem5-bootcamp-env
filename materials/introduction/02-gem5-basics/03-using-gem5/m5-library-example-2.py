import m5
from m5.objects import Root

from gem5.isas import ISA
from gem5.utils.requires import requires
from gem5.resources.resource import obtain_resource
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.simulate.simulator import Simulator

if __name__ == "__m5_main__":
    requires(isa_required=ISA.X86)
    cache_hierarchy = NoCache()
    memory = SingleChannelDDR3_1600(size="32MB")
    processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, isa=ISA.X86,
        num_cores=1)
    board = SimpleBoard(clk_freq="3GHz", processor=processor, memory=memory,
        cache_hierarchy=cache_hierarchy)
    board.set_se_binary_workload(obtain_resource("x86-hello64-static"))
    board._pre_instantiate()

    root = Root(full_system=False, system=board)
    m5.instantiate()
    exit_event = m5.simulate(10**7)

    print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}.")
    print()

    m5.stats.dump()
    m5.stats.reset()
    exit_event = m5.simulate()
    print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}.")
