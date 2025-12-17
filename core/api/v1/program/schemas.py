from datetime import datetime

from ninja import Schema


class ProgramSchema(Schema):
    id: int
    time: str
    title: str
    moderator: str | None
    order: int
    created_at: datetime
