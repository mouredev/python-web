import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
BOUNCEIN_ANIMATION = "animate__animated animate__bounceIn"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;800&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.REGULAR.value,
    "background_color": Color.DARK.value,
    rx.heading: {
        "color": TextColor.LIGHT.value,
        "font_family": Font.DEFAULT.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    # rx.button: {
    #     "width": "100%",
    #     "height": "100%",
    #     "padding": Size.SMALL.value,
    #     "border_radius": Size.DEFAULT.value,
    #     "color": TextColor.LIGHT.value,
    #     "background_color": Color.DARK.value,
    #     "white_space": "normal",
    #     "text_align": "start",
    #     "--cursor-button": "pointer",
    #     "_hover": {
    #         "background_color": Color.PRIMARY.value
    #     }
    # },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "font_weight": FontWeight.MEDIUM.value,
        "cursor": "pointer",
        "white_space": "nowrap",
        "transition": "transform 0.05s ease",
        "color": Color.DARK.value,
        "border": f"1px solid {Color.LIGHT.value}",
        "box_shadow": f"3px 3px 0px 0px {Color.LIGHT.value}",
        "_hover": {
            "color": Color.LIGHT.value,
            "background": Color.DARK.value,
            "box_shadow": "none",
            "transform": "translate(3px, 3px)"
        }
    },
    rx.link: {
        "color": TextColor.LIGHT.value,
        "text_decoration": "none",
        ""
        "_hover": {}
    }
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value,
    font_weight=FontWeight.BOLD.value,
)
