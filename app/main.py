# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI

from app.api.endpoints import (ping, notes)
from app.service.database import (engine, metadata, db)


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

# routing
app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
