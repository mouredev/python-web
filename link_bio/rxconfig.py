import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://api.moure.dev",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://moure.dev"
    ]
)
