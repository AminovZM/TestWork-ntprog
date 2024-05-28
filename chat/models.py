from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()

application = Table(
    "application",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("creation_time", TIMESTAMP, default=datetime.utcnow),
    Column("change_time", TIMESTAMP, default=datetime.utcnow),
    Column("status", String),
    Column("side", String),
    Column("price", Integer),
    Column("amount", Integer),
    Column("instrument", String)
)