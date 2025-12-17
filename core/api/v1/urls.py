from ninja import Router

from core.api.v1.about.handlers import router as about_router
from core.api.v1.partnership.handlers import router as partnership_router
from core.api.v1.previous_meetings.handlers import router as previous_meetings_router
from core.api.v1.program.handlers import router as program_router
from core.api.v1.registrations.handlers import router as registrations_router
from core.api.v1.speakers.handlers import router as speakers_router

router = Router(tags=["v1"])

router.add_router("about/", about_router)
router.add_router("speakers/", speakers_router)
router.add_router("program/", program_router)
router.add_router("previous-meetings/", previous_meetings_router)
router.add_router("partnership/", partnership_router)
router.add_router("registrations/", registrations_router)
