from discord.ext import commands


class ReactOnPing(commands.Cog):
    """Reacts with a ping emoji when someone gets pinged."""

    emojis = ["<:bacle:1214520769011388436>"]

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if len(message.mentions):
            for emoji in self.emojis:
                await message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(ReactOnPing(bot))
