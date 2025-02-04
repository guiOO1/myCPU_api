import pyamdgpuinfo

class GPUReturns():
    def __init__(self):
        self.mygpu = pyamdgpuinfo.get_gpu(0)

    def get_gpu_name(self):
        gpu_name = self.mygpu.name

        return gpu_name

    def get_gpu_mem_info(self):
        gpu_mem_info = self.mygpu.memory_info

        return gpu_mem_info

    def get_gpu_vram_usage(self):
        gpu_vram_usage = self.mygpu.query_vram_usage()

        return gpu_vram_usage

    def get_gpu_temp(self):
        gpu_temperature = self.mygpu.query_temperature()

        return gpu_temperature

    def get_gpu_power_use(self):
        gpu_power = self.mygpu.query_power()

        return gpu_power

    def get_gpu_usage(self):
        gpu_usage = self.mygpu.query_load()

        return gpu_usage