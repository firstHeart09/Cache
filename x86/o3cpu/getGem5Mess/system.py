"""two_ways.py"""
# import m5 library and all SimObjects that we have compiled
import m5
from m5.objects import *
# 导入自定义的cache类
from cache import *
# 导入配置选项
import argparse

parser = argparse.ArgumentParser(description='A simple system with 2-level cache.')
parser.add_argument("--binary", default="", nargs="?", type=str,
                    help="Path to the binary to execute.")
parser.add_argument("--l1i_size",
                    help="L1 instruction cache size. Default: 16kB.")
parser.add_argument("--l1d_size",
                    help="L1 data cache size. Default: Default: 64kB.")
parser.add_argument("--l2_size",
                    help="L2 cache size. Default: 256kB.")
parser.add_argument("--clk",
                    help="CPU clk. Default: 1GHz")
parser.add_argument("--cache_line_size",
                    help="CPU cache line size. Default: 64B")

options = parser.parse_args()


# 创建我们模拟的系统
system = System()

# 设置系统时钟相关信息
# 为该系统设置时钟域
system.clk_domain = SrcClockDomain()
# 在该域上设置时钟频率：1GHz
if not options or not options.clk:
    system.clk_domain.clock = '1GHz'  # 默认时钟周期为1Ghz
else:
    system.clk_domain.clock = options.clk
# 为这个时钟域指定一个电压域
system.clk_domain.voltage_domain = VoltageDomain()

# 设置系统要模拟的内存相关信息
# 设置内存模拟模式为 timing mode
system.mem_mode = 'timing'
# 设置单片内存大小为512MB
system.mem_ranges = [AddrRange('512MB')]

# 设置CPU相关信息
system.cpu = O3CPU()

# 创建L1Cache   L2Cache
system.cpu.icache = L1ICache(options)
system.cpu.dcache = L1DCache(options)
# 将cache连接到CPU上面
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# 创建L2Bus  将L1Cache连接到L2Cache
system.l2bus = L2XBar()
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# 创建L2Cache，将其连接到L2Bus和内存总线
system.l2cache = L2Cache(options)
system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)

# 定义cache line大小
if not options or not options.cache_line_size:
    system.cache_line_size = 64
else:
    system.cache_line_size = options.cache_line_size

#these four lines are to make sure that our system will function correctly
#connecting the PIO and interrupt ports to the memory bus is an x86-specific requirement
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports


# 创建一个内存控制器并连接到内存总线membus上
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports


# 现在我们的整个模拟系统已经构建完成
# binary  要执行的程序编译链接成的二进制文件路径
# options.binary = '/home/dushuai/binutils/gem5/tests/test-progs/hello/bin/x86/linux/hello'

# for gem5 V21 and beyond
# 初始化工作负载
system.workload = SEWorkload.init_compatible(options.binary)
# 创建进程
process = Process()
# 设置 processes 命令添加到我们要运行的命令
process.cmd = [options.binary]
# 设置CPU 将进程process用作工作负载
system.cpu.workload = process
# 创建CPU种的执行上下文
system.cpu.createThreads()

# 实例化系统并开始 执行
root = Root(full_system = False, system = system)
m5.instantiate()

# 开始实际的模拟过程
print("Beginning simulation!")
exit_event = m5.simulate()

# 模拟完成后，显示系统信息
print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))
