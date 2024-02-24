import reflex as rx
import link_bio.utils as utils
from link_bio.api.api import live, featured, schedule
from link_bio.model.Featured import Featured
from link_bio.model.Live import Live

USER = "mouredev"


class PageState(rx.State):

    timezone = ""
    live_status = Live(live=False, title="")
    next_live = ""
    featured_info: list[Featured]

    async def check_live(self):
        self.live_status = await live(USER)

    def check_schedule(self):
        if self.timezone == "":
            return rx.call_script(
                utils.LOCAL_TIMEZONE_SCRIPT,
                PageState.update_timezone
            )
        else:
            self.update_timezone(self.timezone)

    async def update_timezone(self, timezone: str):
        self.timezone = timezone
        self.next_live = utils.next_date(await schedule(), self.timezone)

    async def featured_links(self):
        self.featured_info = await featured()
