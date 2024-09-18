import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.styles.colors import Color
from link_bio.styles.styles import Spacing


def newsletter() -> rx.Component:
    return rx.vstack(
        link_button(
            "mouredev.log",
            "La newsletter de la comunidad para mantenerse al día",
            "/icons/news.svg",
            const.NEWSLETTER_URL
        ),
        rx.html(
            "<iframe src='https://embeds.beehiiv.com/c9c3f7b7-7ed9-428a-a58f-cb53577fa352?slim=true' data-test-id='beehiiv-embed' title='Formulario de suscripción newsletter mouredev pro' width='100%' height='52' frameborder='0' scrolling='no' style='margin: 0; border-radius: 6px !important; background-color: transparent;'></iframe>",
            width="100%"
        ),
        spacing=Spacing.DEFAULT.value,
        width="100%"
    )
