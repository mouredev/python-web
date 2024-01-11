import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
from link_bio.styles.styles import Size


# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-3YGHT3XJFS');
"""
        ),
    ],
)

title = "MoureDev | Te enseño programación y desarrollo de software"
description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."
preview = "https://moure.dev/preview.jpg"

app.add_page(
    index,
    title=title,
    description=description,
    image="avatar.jpg",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@mouredev"}
    ]
)
