import reflex as rx
from link_bio.styles.colors import Color
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Spacing


def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.SMALL.value
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value
                ),
                align_items="start",
                spacing=Spacing.VERY_SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value
            ),
            align="center",
            width="100%"
        ),
        variant="solid",
        radius="none",
        background_color=highlight_color if highlight_color != None else Color.PRIMARY.value,
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, is_external=is_external)
    )
