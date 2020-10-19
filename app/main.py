# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
