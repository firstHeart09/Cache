"""cache.py"""
from m5.objects import Cache

"""
assoc: 每个组中包含的行数

tag_latency: 在执行标签查找时所需的时钟周期数

data_latency: 从缓存中读取数据所需的时钟周期数

response_latency: 在缓存未命中时，返回miss路径的延迟。当cache未命中时，需要从内存中获取数据，这个参数指定了这个返回路径的延迟。

mshrs: 每个缓存的最大请求队列数量
指定了在缓存未命中时可以同时存储的未命中请求的数量。这些未命中请求包括需要从主存中加载的数据。当缓存未命中时，请求将被放置在MSHR中，以等待数据返回。

tgts_per_mshr: 每个MSHR可以同时处理的最大访问数量
指定了每个未命中请求队列（MSHR）可以同时处理的未命中访问数量的上限。当处理器发出多个未命中请求时，这些请求将被放置在MSHR中等待响应。tgts_per_mshr参数确定了在任何给定时间点，MSHR可以同时处理的最大访问数量。
"""

# L1Cache类声明
class L1Cache(Cache):
    def __init__(self, options = None):
        super().__init__()
        self.assoc = 2               # 2路 num of cache line = 2
        self.tag_latency = 2         # 查找标签tag时需要的时钟周期
        self.data_latency = 2        # 从缓存中读取数据所需要的时钟周期
        self.response_latency = 2    # cache未命中时，返回miss路径的延迟
        self.mshrs = 4               # 每个缓存的最大请求队列数量
        self.tgts_per_mshr = 20      # 每个MSHR可以同时处理的最大访问数量

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU-side port
        This must be defined in a subclass"""
        raise NotImplementedErro

    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports


# L1 I-Cache
class L1ICache(L1Cache):
    def __init__(self, options = None):
        super().__init__(options)
        if not options or not options.l1i_size:
            self.size = '16kB'
        else:
            self.size = options.l1i_size
    
    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

# L1 D-Cache
class L1DCache(L1Cache):
    def __init__(self, options = None):
        super().__init__(options)
        if not options or not options.l1d_size:
            self.size = '64kB'
        else:
            self.size = options.l1d_size
    
    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port


# L2Cache类声明
class L2Cache(Cache):
    def __init__(self, options = None):
        super().__init__()
        if not options or not options.l2_size:
            self.size = '256kB'
        else:
            self.size = options.l2_size
        self.assoc = 8
        self.tag_latency = 20
        self.data_latency = 20
        self.response_latency = 20
        self.mshrs = 20
        self.tgts_per_mshr = 12

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports