import reflex as rx
from link_bio.styles.styles import Size as Size


def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.VERY_BIG.value,
            src=imagen
        ),
        href=url,
        is_external=True
    )
