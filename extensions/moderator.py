from discord.ext import commands
import discord


class Moderator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def welcome_msg(self, member: discord.Member):
        description = """
            Welcome to Mythicals Realm!
            Before you can go ahead and chat with the rest of the server,
            we'd like you to read the rules of the server first.
            When you've read the rules,
            please reply to this message with `accept`."""

        return discord.Embed(
            title=f"Thank you for joining {member._user.name}!",
            description=description,
            color=discord.Colour.dark_magenta()
        )

    @commands.Cog.listener(name="on_member_join")
    async def on_member_join(self, member):
        msg = await member.send(embed=self.welcome_msg(member))
        input = await self.bot.wait_for(
            'message',
            check=lambda message: message.author == member
            and message.channel == msg.channel
        )

        if input.content == "accept":
            role = discord.utils.get(member.guild.roles, name="Esper")
            await member.add_roles(role)


def setup(bot):
    bot.add_cog(Moderator(bot))
