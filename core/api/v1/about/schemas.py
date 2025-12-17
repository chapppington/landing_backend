from datetime import datetime

from ninja import Schema


class AboutSchema(Schema):
    id: int
    title: str
    description: str
    order: int
    created_at: datetime
