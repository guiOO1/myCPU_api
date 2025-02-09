import cpuinfo
import psutil

class CPUReturns():
    def __init__(self):
        pass

    def get_cpu_name(self):
        cpu_name = cpuinfo.get_cpu_info()['brand_raw']

        return cpu_name

    def get_cpu_percent(self):
        cpu_percent = psutil.cpu_percent(interval=1)

        return cpu_percent

    def get_cpu_freq(self):
        cpu_freq = psutil.cpu_freq()

        return int(list(cpu_freq)[0])