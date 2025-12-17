from typing import Iterable

from core.apps.partnership.models import PartnershipModel


class PartnershipService:
    @staticmethod
    def get_all() -> Iterable[PartnershipModel]:
        return PartnershipModel.objects.all()
