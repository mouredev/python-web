import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button('twitch', "https://www.twitch.tv"),
        link_button("youtube","https://www.youtube.com"),
        link_button("Discord", "https://www.discord.gg"),
        link_button("twitter", "https://www.twitter.com"),
    )
    