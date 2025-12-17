from typing import Any, Generic, TypeVar

from ninja import Schema

TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class PingResponseSchema(Schema):
    response: bool


class ListResponse(Schema, Generic[TListItem]):
    items: list[TListItem]


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = {}
    meta: dict[str, Any] = {}
    errors: list[Any] = []
