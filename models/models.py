from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, TIMESTAMP, ForeignKey

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registred_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
