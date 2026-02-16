import reflex as rx

import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio import utils
from link_bio.api.api import fastapi_app
from link_bio.pages.courses import courses  # noqa: F401
from link_bio.pages.index import index  # noqa: F401

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    api_transformer=fastapi_app,
    head_components=[
        rx.script(src=utils.BEEHIIV_SCRIPT, async_=True),
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
        rx.script(
            """
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '509505096385581');
fbq('track', 'PageView');
"""
        ),
        rx.el.noscript(
            rx.image(
                height="1",
                width="1",
                style={"display": "none"},
                src="https://www.facebook.com/tr?id=509505096385581&ev=PageView&noscript=1",
            ),
        ),
    ],
)
