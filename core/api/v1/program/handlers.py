from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.program.schemas import ProgramSchema
from core.apps.program.service import ProgramService

router = Router(tags=["program"])


@router.get("", response=ApiResponse[ListResponse[ProgramSchema]])
def get_program_list_handler(request: HttpRequest):
    items = [ProgramSchema.model_validate(item) for item in ProgramService.get_all()]
    return ApiResponse[ListResponse[ProgramSchema]](
        data=ListResponse[ProgramSchema](items=items),
    )
