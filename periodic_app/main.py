from apscheduler.schedulers.asyncio import AsyncIOScheduler
from periodic_app.clearing_request_limit import cleaner
from utils.config import cleaning_frequency


async def planned_machine(*args) -> None:
    """Функция по установке условий для периодических приложений"""

        # Инициализация класса
    scheduler = AsyncIOScheduler()

    scheduler.add_job(cleaner, 'interval', seconds=cleaning_frequency)

    scheduler.start()
