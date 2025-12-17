from datetime import datetime

from ninja import Schema


class RegistrationCreateSchema(Schema):
    name: str
    email: str
    phone: str
    comments: str | None = None
    consent: bool


class RegistrationsSchema(Schema):
    id: int
    name: str
    email: str
    phone: str
    comments: str | None
    consent: bool
    created_at: datetime


class RegistrationResponseSchema(Schema):
    success: bool
    message: str
    data: RegistrationsSchema | None = None
