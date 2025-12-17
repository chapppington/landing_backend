from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.previous_meetings.schemas import PreviousMeetingsSchema
from core.apps.previous_meetings.service import PreviousMeetingsService

router = Router(tags=["previous-meetings"])


@router.get("", response=ApiResponse[ListResponse[PreviousMeetingsSchema]])
def get_previous_meetings_list_handler(request: HttpRequest):
    items = [
        PreviousMeetingsSchema.model_validate(item)
        for item in PreviousMeetingsService.get_all()
    ]
    return ApiResponse[ListResponse[PreviousMeetingsSchema]](
        data=ListResponse[PreviousMeetingsSchema](items=items),
    )
