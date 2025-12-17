from typing import Iterable

from django.db.models import Q

from core.apps.registrations.models import RegistrationsModel


class RegistrationsService:
    @staticmethod
    def get_all() -> Iterable[RegistrationsModel]:
        return RegistrationsModel.objects.all()

    @staticmethod
    def normalize_string(value: str) -> str:
        return value.lower().strip()

    @staticmethod
    def check_duplicate(name: str, email: str, phone: str) -> bool:
        normalized_name = RegistrationsService.normalize_string(name)
        normalized_email = RegistrationsService.normalize_string(email)
        normalized_phone = RegistrationsService.normalize_string(phone)

        return RegistrationsModel.objects.filter(
            Q(name__iexact=normalized_name)
            & Q(email__iexact=normalized_email)
            & Q(phone__iexact=normalized_phone),
        ).exists()

    @staticmethod
    def create(
        name: str,
        email: str,
        phone: str,
        comments: str | None,
        consent: bool,
    ) -> RegistrationsModel:
        if RegistrationsService.check_duplicate(name, email, phone):
            raise ValueError("Пользователь с такими данными уже зарегистрирован")

        return RegistrationsModel.objects.create(
            name=name,
            email=email,
            phone=phone,
            comments=comments or "",
            consent=consent,
        )
