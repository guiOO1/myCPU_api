import mysql.connector

from components_returns.cpu_returns import CPUReturns
from components_returns.gpu_returns import GPUReturns
from components_returns.motherboard_returns import MotherboardReturns
from components_returns.ram_mem_returns import MemRamReturns

class InsertData():

    def __init__(self):
        self.GPU_RETURNS = GPUReturns()
        self.CPU_RETURNS = CPUReturns()
        self.MOTHERBOARD_RETURNS = MotherboardReturns()
        self.MEM_RAM_RETURNS = MemRamReturns()

    def insert_all_data(self):
        self.insert_all_gpu_data()
        self.insert_all_cpu_data()
        self.insert_all_motherboard_data()
        self.insert_all_mem_ram_data()

    def insert_all_gpu_data(self):
        pass

    def insert_all_cpu_data(self):
        pass

    def insert_all_motherboard_data(self):
        pass

    def insert_all_mem_ram_data(self):
        pass