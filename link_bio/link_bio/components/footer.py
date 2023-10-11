import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            "Github @Garosoro",
            href="https://github.com",
            is_external=True
        ),
        rx.text(f"© {datetime.date.today().year} link.bio")
    )