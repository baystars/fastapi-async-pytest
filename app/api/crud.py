# -*- mode: python -*- -*- coding: utf-8 -*-
from app.api.schemas import NoteSchema
from app.api.models import Notes
from app.database import db


async def post(payload: NoteSchema):
    query = Notes.insert().values(title=payload.title, description=payload.description)
    return await db.execute(query=query)
