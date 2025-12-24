import reflex as rx

from link_bio import conf
from link_bio.lib.snow import snow
from link_bio.routes import Route
from link_bio.styles.colors import Color
from link_bio.styles.styles import Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="/logo.svg",
                width="auto",
                height=Size.LARGE.value,
                justify="start",
                alt="MoureDev logo",
            ),
            href=Route.INDEX.value,
        ),
        rx.cond(conf.SNOW, snow()),
        position="sticky",
        bg=Color.DARK.value,
        border_bottom="1px solid rgba(247, 247, 247, 0.2)",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
