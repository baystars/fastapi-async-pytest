# -*- mode: python -*- -*- coding: utf-8 -*-
import os

from databases import Database
from sqlalchemy import (create_engine, MetaData)


DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./data/data.db"
#DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///data.db"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# databases query builder
db = Database(DATABASE_URL)
