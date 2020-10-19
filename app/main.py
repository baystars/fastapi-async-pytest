# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}
