from datetime import datetime

from ninja import Schema


class PartnershipSchema(Schema):
    id: int
    title: str
    description: str
    image: str | None
    order: int
    created_at: datetime
