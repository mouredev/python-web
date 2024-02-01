import link_bio.constants as const
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()


async def repo() -> str:
    return const.REPO_URL


async def live(user: str) -> bool:
    return TWITCH_API.live(user)
