# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI

from app.api import ping

app = FastAPI()


app.include_router(ping.router)
