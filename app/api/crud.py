# -*- mode: python -*- -*- coding: utf-8 -*-
from app.api.schemas import NoteSchema
from app.api.models import Notes
from app.database import db


async def post(payload: NoteSchema):
    query = Notes.insert().values(title=payload.title, description=payload.description)
    return await db.execute(query=query)


async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)
