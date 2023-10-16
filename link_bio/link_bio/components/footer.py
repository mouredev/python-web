import reflex as rx
import datetime

<<<<<<< HEAD
=======

>>>>>>> 1c6e03baf4d8fb00f2cacc6019009d769f09600c
def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2014-{datetime.date.today().year} MOUREDEV BY BRAIS MOURE V3.",
            href="https://mouredev.com",
            is_external=True
        ),
        rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.")
    )
