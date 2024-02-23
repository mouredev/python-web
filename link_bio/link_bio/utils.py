from datetime import date, datetime, timedelta, timezone
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

    if len(dates) == 0:
        return ""

    now = datetime.now()
    current_weekday = now.weekday()
    current_time = now.astimezone().timetz()

    for index in range(7):

        day = str((current_weekday + index) % 7)

        if day not in dates or dates[day] == "":
            continue

        time_utc = datetime.strptime(
            dates[day],
            "%H:%M"
        ).replace(tzinfo=timezone.utc).timetz()

        time = datetime.combine(now.date(), time_utc).astimezone().timetz()

        if current_time < time or index > 0:

            next_date = now + timedelta(days=index)

            formatted_next_date = next_date.strftime(
                "Hoy, %d/%m") if index == 0 else next_date.strftime("%A, %d/%m")
            formatted_next_time = time.strftime("%H:%M")

            return f"{formatted_next_date} a las {formatted_next_time} ({dates[day]} UTC)"

    return ""
