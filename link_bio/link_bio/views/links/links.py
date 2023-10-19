import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "https://twitch.tv/mouredev"
        ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            "https://youtube.com/@mouredev"
        ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            "https://youtube.com/@mouredevtv"
        ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discrod.gg/mouredev"
        ),
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "https://twitch.tv/mouredev"
        ),
        link_button(
            "YouTube",
            "Tutoriales semanales",
            "https://youtube.com/@mouredev"
        ),
        link_button(
            "YouTube (canal secundario)",
            "Tutoriales semanales",
            "https://youtube.com/@mouredevtv"
        ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discrod.gg/mouredev"
        ),
        width="100%",
        spacing=Size.MEDIUM.value,
    )
