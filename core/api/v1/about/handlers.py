from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.about.schemas import AboutSchema
from core.apps.about.service import AboutService

router = Router(tags=["about"])


@router.get("", response=ApiResponse[ListResponse[AboutSchema]])
def get_about_list_handler(request: HttpRequest):
    items = [AboutSchema.model_validate(item) for item in AboutService.get_all()]
    return ApiResponse[ListResponse[AboutSchema]](
        data=ListResponse[AboutSchema](items=items),
    )
