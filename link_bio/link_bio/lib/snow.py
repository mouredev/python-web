import reflex as rx


class Snowflakes(rx.Component):
    tag = "Snowflakes"
    library = "/public/js/snowflakes.js"


snowflakes = Snowflakes.create


def snow() -> rx.Component:
    return rx.el.div(
        rx.el.p("*", class_name="snowflake"),
        snowflakes(),
        id="SnowflakeContainer",
        aria_hidden="true",
    )
