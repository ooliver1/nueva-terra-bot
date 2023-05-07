from __future__ import annotations

from botbase import BotBase
from nextcord import Intents, MemberCacheFlags

__all__ = ("NuevaTerra",)


class NuevaTerra(BotBase):
    def __init__(self) -> None:
        super().__init__(
            intents=Intents(guilds=True),
            member_cache_flags=MemberCacheFlags.none(),
            guild_ids=[802586580766162964],
            log_channel=921139782648725515,
        )
