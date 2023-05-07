from __future__ import annotations

from botbase import CogBase
from nextcord import Permissions, TextChannel, slash_command
from ormar import NoMatch

from nueva_terra.bot import NuevaTerra
from nueva_terra.db import Message
from nueva_terra.image import generate_content
from nueva_terra.inter import Inter


class Initialise(CogBase[NuevaTerra]):
    @slash_command(default_member_permissions=Permissions(administrator=True))
    async def initialise(self, inter: Inter, channel: TextChannel) -> None:
        file, embed = generate_content()

        message = await channel.send(file=file, embed=embed)
        await inter.send(f"Initialised timer. {message.jump_url}", ephemeral=True)

        try:
            record = await Message.objects.get(channel_id=channel.id)
        except NoMatch:
            await Message.objects.create(
                channel_id=channel.id, message_id=message.id, time=message.created_at
            )
        else:
            await record.update(message_id=message.id, time=message.created_at)


def setup(bot: NuevaTerra) -> None:
    bot.add_cog(Initialise(bot))
