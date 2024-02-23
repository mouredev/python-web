import reflex as rx
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import repo, live, featured, schedule

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)
app.api.add_api_route("/featured", featured)
app.api.add_api_route("/schedule", schedule)
