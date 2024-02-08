import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Color


def link_button(title: str, body: str, image: str, url: str, is_external=True, highlight_color=None) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            ),
            border_color=highlight_color,
            border_width="2px" if highlight_color != None else None
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
