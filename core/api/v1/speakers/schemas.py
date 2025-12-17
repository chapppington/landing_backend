from datetime import datetime

from ninja import Schema


class SpeakersSchema(Schema):
    id: int
    name: str
    position: str
    image: str | None
    order: int
    created_at: datetime
