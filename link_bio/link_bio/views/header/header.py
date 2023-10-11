import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Garosoro", size="xl"),
        rx.text("@garosoro"),
        rx.text("Hola, soy Gabriel Soto Rojas "),
        rx.text("Tecnico en computacion e infomatica, gustos por la programacion y el desarrollo web y ciencia de datos, actualmente estudiante de ingenieria de software"),

    )