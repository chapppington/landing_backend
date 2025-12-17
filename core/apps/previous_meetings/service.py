from typing import Iterable

from core.apps.previous_meetings.models import PreviousMeetingsModel


class PreviousMeetingsService:
    @staticmethod
    def get_all() -> Iterable[PreviousMeetingsModel]:
        return PreviousMeetingsModel.objects.all()
