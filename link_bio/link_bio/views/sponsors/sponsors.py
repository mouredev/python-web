import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "elgato.png",
                const.ELGATO_URL
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL
            ),
            spacing=Size.BIG.value
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
