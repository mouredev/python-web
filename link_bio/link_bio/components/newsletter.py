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
            "<iframe src='https://subscribe-forms.beehiiv.com/84ec1259-e16b-41b4-be33-d1f2dd2cf53e' class='beehiiv-embed' data-test-id='beehiiv-embed' title='Formulario de suscripción newsletter mouredev' width='100%' height='110px' frameborder='0' scrolling='no' allowtransparency='true' style='width: 100%; height: 110px; margin: 0; border-radius: 0px !important; background-color: transparent; color-scheme: normal;'></iframe>",
            width="100%",
            height="100px",
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
