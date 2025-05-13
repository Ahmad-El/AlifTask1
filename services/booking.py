from datetime import timedelta
from db.models import Cabin, Reservation
from db.session import SessionLocal
from notifications.email_sender import send_email
from notifications.sms_sender import send_sms

session = SessionLocal()


def check_availability(cabin_number, check_time):
    cabin = session.query(Cabin).filter_by(number=cabin_number).first()
    if not cabin:
        return f"Кабинет {cabin_number} не существует."

    reservation = (
        session.query(Reservation)
        .filter(
            Reservation.cabin_id == cabin.id,
            Reservation.start_time <= check_time,
            Reservation.end_time >= check_time,
        )
        .first()
    )

    if reservation:
        return f"Кабинет {cabin_number} занят до {reservation.end_time} кем: {reservation.user_name}"
    return f"Кабинет {cabin_number} свободен на {check_time}"


def reserve_cabin(
    cabin_number, user_name, user_email, user_phone, start_time, duration_minutes
):
    cabin = session.query(Cabin).filter_by(number=cabin_number).first()
    if not cabin:
        return f"Кабинет {cabin_number} не существует."

    end_time = start_time + timedelta(minutes=duration_minutes)

    reservation = (
        session.query(Reservation)
        .filter(
            Reservation.cabin_id == cabin.id,
            Reservation.start_time <= end_time,
            Reservation.end_time >= start_time,
        )
        .first()
    )

    if reservation:
        return f"Кабинет {cabin_number} уже занят в это время."

    new_reservation = Reservation(
        cabin_id=cabin.id,
        user_name=user_name,
        user_email=user_email,
        user_phone=user_phone,
        start_time=start_time,
        end_time=end_time,
    )
    session.add(new_reservation)
    session.commit()

    message = f"Вы забронировали кабинет {cabin_number} с {start_time} до {end_time}"
    send_email(user_email, "Подтверждение бронирования", message)
    send_sms(user_phone, message)

    return f"Кабинет {cabin_number} успешно забронирован."
