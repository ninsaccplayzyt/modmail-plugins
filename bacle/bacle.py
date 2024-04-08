from discord.ext import commands


class Banana(commands.Cog):
    """Reacts with a banana emoji if someone says banana."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "BACLE" in message.content.upper():
            emoji_id = 1214520769011388436
            custom_emoji = f"<:bacle:{emoji_id}>"
            await message.add_reaction(custom_emoji)


def setup(bot):
    bot.add_cog(Banana(bot))
