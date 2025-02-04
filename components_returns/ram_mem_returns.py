import psutil
from psutil._common import bytes2human

class RamMemReturns():
    def __init__(self):
        pass

    def get_ram_mem_total(self):
        total_mem = psutil.virtual_memory().total

        total_mem = bytes2human(total_mem)

        return total_mem

    def get_ram_mem_available(self):
        available_mem = psutil.virtual_memory().available

        available_mem = bytes2human(available_mem)

        return available_mem

    def get_ram_mem_active(self):
        active_mem = psutil.virtual_memory().available

        active_mem = bytes2human(active_mem)

        return active_mem

    def get_ram_mem_percent(self):
        percent_mem = psutil.virtual_memory().available

        percent_mem = bytes2human(percent_mem)

        return active_mem
