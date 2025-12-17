from typing import Iterable

from core.apps.speakers.models import SpeakersModel


class SpeakersService:
    @staticmethod
    def get_all() -> Iterable[SpeakersModel]:
        return SpeakersModel.objects.all()
