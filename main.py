from apscheduler.schedulers.background import BackgroundScheduler

from fastapi import FastAPI
import asyncio

import database_init


API_APP = FastAPI()

@API_APP.get("/test")
async def test():
    return "data"
