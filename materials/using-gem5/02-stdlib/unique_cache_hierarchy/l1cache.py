from m5.objects import Cache, StridePrefetcher


class L1Cache(Cache):
    def __init__(self):
        super().__init__()
        self.size = "32KiB"
        self.assoc = 8
        self.tag_latency =1
        self.data_latency = 1
        self.response_latency = 1
        self.mshrs = 16
        self.tgts_per_mshr = 20
        self.writeback_clean = True
        self.prefetcher = StridePrefetcher()
