from datetime import datetime, timedelta, timezone
import pytz
import locale
import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]

# Index

index_title = "MoureDev | Te enseño programación y desarrollo de software"
index_description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos

courses_title = "MoureDev | Cursos gratis de programación"
courses_description = "Este es un listado con algunos cursos gratis para aprender programación y desarrollo de software. Python, SQL, Git..."

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)

# Date


def next_date(dates: dict) -> str:

    # Se fuerza el locale para traducir el formateo de fecha a español
    # locale.setlocale(locale.LC_TIME, "es_ES")

    if len(dates) == 0:
        return ""

    now = datetime.now()
    current_time = now.astimezone().timetz()

    for weekday in range(7):

        current_weekday = str((now.weekday() + weekday) % 7)

        if current_weekday not in dates or dates[current_weekday] == "":
            continue

        time_utc = datetime.strptime(dates[current_weekday], "%H:%M").replace(
            tzinfo=pytz.UTC).timetz()

        next_time = datetime.combine(
            now.date(), time_utc).astimezone().timetz()

        if current_time < next_time or weekday > 0:

            next_date = now + timedelta(days=weekday)

            local_date = datetime(
                next_date.year, next_date.month, next_date.day,
                time_utc.hour, time_utc.minute, tzinfo=pytz.UTC).astimezone()

            return local_date.strftime("%A, %d de %B a las %H:%M").capitalize()

    return ""
