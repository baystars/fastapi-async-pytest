# -*- mode: python -*- -*- coding: utf-8 -*-
from app.api.schemas import NoteSchema
from app.api.models import Notes
from app.database import db


async def post(payload: NoteSchema):
    query = Notes.insert().values(title=payload.title, description=payload.description)
    return await db.execute(query=query)


async def get(id: int):
    query = notes.select().where(id==notes.c.id)
    return await db.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await db.fetch_all(query=query)


async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await db.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
