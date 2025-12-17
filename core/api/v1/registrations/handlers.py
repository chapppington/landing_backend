from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse, ListResponse
from core.api.v1.registrations.schemas import (
    RegistrationCreateSchema,
    RegistrationResponseSchema,
    RegistrationsSchema,
)
from core.apps.registrations.service import RegistrationsService
from core.apps.registrations.tasks import send_registration_email

router = Router(tags=["registrations"])


@router.get("", response=ApiResponse[ListResponse[RegistrationsSchema]])
def get_registrations_list_handler(request: HttpRequest):
    items = [
        RegistrationsSchema.model_validate(item)
        for item in RegistrationsService.get_all()
    ]
    return ApiResponse[ListResponse[RegistrationsSchema]](
        data=ListResponse[RegistrationsSchema](items=items),
    )


@router.post("", response=RegistrationResponseSchema)
def create_registration_handler(request: HttpRequest, data: RegistrationCreateSchema):
    try:
        registration = RegistrationsService.create(
            name=data.name,
            email=data.email,
            phone=data.phone,
            comments=data.comments,
            consent=data.consent,
        )

        send_registration_email(
            name=data.name,
            email=data.email,
            phone=data.phone,
            comments=data.comments,
        )

        return RegistrationResponseSchema(
            success=True,
            message="Регистрация успешно сохранена",
            data=RegistrationsSchema.model_validate(registration),
        )
    except ValueError as e:
        raise HttpError(409, str(e))
    except Exception as e:
        raise HttpError(500, f"Ошибка при сохранении данных: {str(e)}")
