import reflex as rx

import link_bio.constants as const
from link_bio.components.featured_link import featured_link
from link_bio.components.link_button import link_button
from link_bio.components.newsletter import newsletter
from link_bio.components.title import title
from link_bio.routes import Route
from link_bio.state.PageState import PageState
from link_bio.styles.styles import Color, Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Curso gratis de Desarrollo con IA",
            "Apúntate a mi curso 100% gratis, online y con certificado",
            "/icons/logo_symbol.svg",
            "https://mouredev.link/cursodesarrolloia",
            True,
            Color.GREEN.value,
            animated=True
        ),
        link_button(
            "mouredev pro",
            "Estudia programación de manera diferente",
            "/icons/pro.svg",
            const.PRO_URL,
            True,
            Color.ORANGE.value
        ),
        link_button(
            "Cursos gratis",
            "Consulta mis tutoriales para aprender programación",
            "/icons/code.svg",
            Route.COURSES.value,
            False,
            Color.YELLOW.value,
        ),
        # link_button(
        #     "Guías de programación",
        #     "Mi listado de guías gratis en PDF para aprender desarrollo",
        #     "/icons/book.svg",
        #     const.RESOURCES_URL,
        #     True,
        #     Color.GREEN.value
        # ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "YouTube",
            "Cursos y tutoriales sobre desarrollo de software",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        title("Newsletter"),
        newsletter(),
        rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Destacado"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value
                ),
                spacing=Spacing.DEFAULT.value
            )
        ),
        title("Recursos y más"),
        link_button(
            "Git y GitHub desde cero",
            "Aquí puedes comprar mi libro en formato físico y eBook",
            "/icons/git.svg",
            const.BOOK_URL
        ),
        link_button(
            "Twitch",
            "Transmisiones sobre programación y desarrollo",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube | canal secundario",
            "Emisiones en directo destacadas",
            "/icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        # link_button(
        #     "Libros recomendados",
        #     "Mi listado de libros sobre programación, ciencia y tecnología",
        #     "/icons/book.svg",
        #     const.BOOKS_URL
        # ),
        # link_button(
        #     "Mi setup",
        #     "Listado con todos los elementos que uso en mi trabajo",
        #     "/icons/setup.svg",
        #     const.SETUP_URL
        # ),
        # link_button(
        #     "MoureDev",
        #     "Mi sitio web",
        #     "/icons/logo_symbol.svg",
        #     const.MOUREDEV_URL
        # ),
        link_button(
            "Invítame a un café",
            "¿Quieres ayudarme a que siga creando contenido?",
            "/icons/coffee.svg",
            const.COFFEE_URL
        ),

        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "/icons/checkemail.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=PageState.featured_links
    )
