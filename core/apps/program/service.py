from typing import Iterable

from core.apps.program.models import ProgramModel


class ProgramService:
    @staticmethod
    def get_all() -> Iterable[ProgramModel]:
        return ProgramModel.objects.all()
