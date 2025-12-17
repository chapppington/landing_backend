from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.speakers.schemas import SpeakersSchema
from core.apps.speakers.service import SpeakersService

router = Router(tags=["speakers"])


@router.get("", response=ApiResponse[ListResponse[SpeakersSchema]])
def get_speakers_list_handler(request: HttpRequest):
    items = [SpeakersSchema.model_validate(item) for item in SpeakersService.get_all()]
    return ApiResponse[ListResponse[SpeakersSchema]](
        data=ListResponse[SpeakersSchema](items=items),
    )
