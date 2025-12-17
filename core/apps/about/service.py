from typing import Iterable

from core.apps.about.models import AboutModel


class AboutService:
    @staticmethod
    def get_all() -> Iterable[AboutModel]:
        return AboutModel.objects.all()
