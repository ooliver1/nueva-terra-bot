from __future__ import annotations

from os import environ

from botbase import BotBase
from nextcord import Intents, MemberCacheFlags

__all__ = ("NuevaTerra",)


class NuevaTerra(BotBase):
    def __init__(self) -> None:
        super().__init__(
            intents=Intents(guilds=True),
            member_cache_flags=MemberCacheFlags.none(),
            guild_ids=[int(environ["DEBUG_GUILD_ID"])],
            log_channel=int(environ["LOG_CHANNEL_ID"]),
        )
