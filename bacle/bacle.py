from discord.ext import commands

class Bacle(commands.Cog):
    """Reacts with a bacle emoji if someone says bacle."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if "BACLE" in message.content.upper():
            # Replace '1214520769011388436' with the ID of your custom emoji
            emoji_id = 1214520769011388436
            custom_emoji = f"<:bacle:{emoji_id}>"
            await message.add_reaction(custom_emoji)

def setup(bot):
    bot.add_cog(Bacle(bot))
