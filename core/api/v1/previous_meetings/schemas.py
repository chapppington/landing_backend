from datetime import datetime

from ninja import Schema


class PreviousMeetingsSchema(Schema):
    id: int
    image: str
    order: int
    created_at: datetime
