import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://moure.dev"
    ],
    tailwind=None,
    show_built_with_reflex=False
)
