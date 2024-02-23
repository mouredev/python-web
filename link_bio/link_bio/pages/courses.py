import reflex as rx
import link_bio.utils as utils
import link_bio.styles.styles as styles
from link_bio.routes import Route
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.views.sponsors import sponsors
from link_bio.styles.styles import Size
from link_bio.state.PageState import PageState


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )
