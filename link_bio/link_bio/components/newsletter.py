import reflex as rx

import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.styles.colors import TextColor
from link_bio.styles.styles import Spacing


def newsletter() -> rx.Component:
    return rx.vstack(
        link_button(
            "mouredev.log();",
            "La newsletter de la comunidad para aprender, crecer y avanzar",
            "/icons/news.svg",
            const.NEWSLETTER_URL,
        ),
        rx.html(
            "<iframe src='https://embeds.beehiiv.com/c9c3f7b7-7ed9-428a-a58f-cb53577fa352?slim=true' data-test-id='beehiiv-embed' title='Formulario de suscripción newsletter mouredev pro' width='100%' height='52' frameborder='0' scrolling='no' style='margin: 0; border-radius: 6px !important; background-color: transparent;'></iframe>",
            width="100%",
        ),
        rx.hstack(
            rx.icon("mail-check"),
            rx.text(
                "Más de 100.000 personas ya siguen mis consejos semanales",
                color=TextColor.LIGHT.value,
                size=Spacing.MEDIUM_SMALL.value,
            ),
            align="center",
        ),
        spacing=Spacing.DEFAULT.value,
        width="100%",
    )
