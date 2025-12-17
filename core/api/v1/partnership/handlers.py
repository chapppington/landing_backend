from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.partnership.schemas import PartnershipSchema
from core.apps.partnership.service import PartnershipService

router = Router(tags=["partnership"])


@router.get("", response=ApiResponse[ListResponse[PartnershipSchema]])
def get_partnership_list_handler(request: HttpRequest):
    items = [
        PartnershipSchema.model_validate(item) for item in PartnershipService.get_all()
    ]
    return ApiResponse[ListResponse[PartnershipSchema]](
        data=ListResponse[PartnershipSchema](items=items),
    )
