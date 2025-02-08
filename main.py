from fastapi import FastAPI
import asyncio

import mysql.connector

from components_returns.cpu_returns import CPUReturns
from components_returns.gpu_returns import GPUReturns
from components_returns.motherboard_returns import MotherboardReturns
from components_returns.ram_mem_returns import RamMemReturns

import database_init


API_APP = FastAPI()

@API_APP.get("/gpu_temp")
async def read_gpu_temp():
    data = GPUReturns().get_gpu_temp()
    return data
