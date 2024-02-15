from enum import Flag
import reflex as rx
from link_bio.api.api import live, featured
from link_bio.model.Featured import Featured
from link_bio.model.Live import Live

USER = "mouredev"


class PageState(rx.State):

    live_status = Live(live=False, title="")
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live(USER)

    async def featured_links(self):
        self.featured_info = await featured()
