# SPDX-License-Identifier: MIT

from __future__ import annotations

from logging import getLogger
from os import environ

import uvloop

from .bot import NuevaTerra

bot = NuevaTerra()
log = getLogger("nueva_terra")
log.setLevel(environ["LOG_LEVEL"])

if __name__ == "__main__":
    uvloop.install()
    bot.run(environ["TOKEN"])
