import pyamdgpuinfo

class GPUReturns():
    def __init__(self):
        self.mygpu = pyamdgpuinfo.get_gpu(0)

    def get_gpu_name(self):
        gpu_name = self.mygpu.name

        return gpu_name

    def get_gpu_vram_total(self):
        gpu_mem_info = self.mygpu.memory_info['vram_size']

        return "%.2f"%(gpu_mem_info / 1024 / 1024 / 1024)

    def get_gpu_vram_usage(self):
        gpu_vram_usage = self.mygpu.query_vram_usage()

        return "%.2f"%(gpu_vram_usage / 1024 / 1024 / 1024)

    def get_gpu_temperature(self):
        gpu_temperature = self.mygpu.query_temperature()

        return gpu_temperature

    def get_gpu_power_use(self):
        gpu_power = self.mygpu.query_power()

        return gpu_power

    def get_gpu_usage(self):
        gpu_usage = self.mygpu.query_load()

        return int(gpu_usage * 100)