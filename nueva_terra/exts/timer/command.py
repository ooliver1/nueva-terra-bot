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
    async def timers(self, inter: Inter) -> None:
        ...

    @timers.subcommand(name="new")
    async def timers_new(self, inter: Inter, channel: TextChannel) -> None:
        """Create a new auto-updating timer, in a given channel.

        This will overwrite any existing timer in the channel.

        channel:
            The channel to create the timer in.
        """
        file, embed = generate_content()

        message = await channel.send(file=file, embed=embed)
        await inter.send(f"Initialised timer: {message.jump_url}", ephemeral=True)

        try:
            record = await Message.objects.get(channel_id=channel.id)
        except NoMatch:
            await Message.objects.create(
                channel_id=channel.id, message_id=message.id, time=message.created_at
            )
        else:
            await record.update(message_id=message.id, time=message.created_at)

    @timers.subcommand(name="delete")
    async def timers_delete(self, inter: Inter, channel: TextChannel) -> None:
        """Delete an existing auto-updating timer, in a given channel.

        channel:
            The channel to delete the timer from.
        """
        try:
            record = await Message.objects.get(channel_id=channel.id)
        except NoMatch:
            await inter.send("No timer initialised for this channel.", ephemeral=True)
        else:
            message = channel.get_partial_message(record.message_id)
            await message.delete()
            await record.delete()
            await inter.send("Deleted timer.", ephemeral=True)


def setup(bot: NuevaTerra) -> None:
    bot.add_cog(Initialise(bot))
