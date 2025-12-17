import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_registration_email(name: str, email: str, phone: str, comments: str | None):
    logger.info(f"Начало отправки письма на {email} для {name}")

    from_email = settings.DEFAULT_FROM_EMAIL or settings.EMAIL_HOST_USER
    if not from_email:
        logger.warning("Email не отправлен: не настроен DEFAULT_FROM_EMAIL")
        return

    logger.info(
        f"Настройки email: HOST={settings.EMAIL_HOST}, PORT={settings.EMAIL_PORT}, "
        f"USE_TLS={getattr(settings, 'EMAIL_USE_TLS', False)}, "
        f"USE_SSL={getattr(settings, 'EMAIL_USE_SSL', False)}, "
        f"USER={settings.EMAIL_HOST_USER}, FROM={from_email}",
    )

    subject = "Регистрация на мероприятие"
    message = f"""
Здравствуйте, {name}!

Ваша регистрация на мероприятие успешно принята.

Ваши данные:
- Имя: {name}
- Email: {email}
- Телефон: {phone}
{f"- Комментарий: {comments}" if comments else ""}

Мы свяжемся с вами в ближайшее время.
"""
    logger.debug(f"Отправка письма с {from_email} на {email}")
    try:
        result = send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[email],
            fail_silently=False,
        )
        if result == 1:
            logger.info(f"Письмо успешно отправлено на {email} (отправлено: {result})")
        else:
            logger.warning(f"Письмо не отправлено на {email} (результат: {result})")
    except Exception as e:
        logger.error(f"Ошибка при отправке письма на {email}: {str(e)}", exc_info=True)
