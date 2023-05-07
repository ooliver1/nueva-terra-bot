# pyright: reportGeneralTypeIssues=false
from __future__ import annotations

from typing import TYPE_CHECKING

from botbase import BaseMeta
from ormar import BigInteger, DateTime, Model

if TYPE_CHECKING:
    from datetime import datetime


class Message(Model):
    class Meta(BaseMeta):
        ...

    channel_id: int = BigInteger(primary_key=True, autoincrement=False)
    message_id: int = BigInteger()
    time: datetime = DateTime(timezone=True)
