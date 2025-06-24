import link_bio.constants as const
from fastapi import FastAPI
from link_bio.model.Featured import Featured
from link_bio.model.Live import Live
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from .ConfigCatAPI import ConfigCatAPI

# API

fastapi_app = FastAPI()

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()
CONFIGCAT_API = ConfigCatAPI()


@fastapi_app.get("/repo")
async def repo() -> str:
    return const.REPO_URL


@fastapi_app.get("/live/{user}")
async def live(user: str) -> Live:
    return TWITCH_API.live(user)


@fastapi_app.get("/featured")
async def featured() -> list[Featured]:
    return SUPABASE_API.featured()


@fastapi_app.get("/schedule")
async def schedule() -> dict:
    return CONFIGCAT_API.schedule()
