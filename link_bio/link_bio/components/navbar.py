import reflex as rx
import link_bio.styles.styles as styles
from link_bio.routes import Route
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("moure", as_="span", color=Color.PRIMARY.value),
                rx.text("dev", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
