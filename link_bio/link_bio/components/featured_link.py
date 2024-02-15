import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size
from link_bio.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=Size.DEFAULT.value
            ),
            rx.text(
                featured.title,
                style=styles.button_body_style
            ),
            spacing=Size.SMALL.value,
            align_items="start"
        ),
        href=featured.url,
        is_external=True
    )
