import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "mouredev",
            height="40px"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )
