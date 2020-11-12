from discord.ext import commands
from helpers.dev import Dev

dev = Dev()


class Management(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx: commands.Context, extension):
        if dev.is_developer(ctx.author.id):
            try:
                self.bot.load_extension(extension)
                await ctx.send(embed=dev.success(
                    f"Extension `{extension}` loaded!"))
            except Exception as e:
                await ctx.send(embed=dev.error(e))
                return
        else:
            await ctx.send(embed=dev.not_dev())

    @commands.command()
    async def unload(self, ctx: commands.Context, extension):
        if dev.is_developer(ctx.author.id):
            self.bot.unload_extension(extension)
            await ctx.send(embed=dev.success(
                f"Extension `{extension}` unloaded!"))
        else:
            await ctx.send(embed=dev.not_dev())

    @commands.command()
    async def reload(self, ctx: commands.Context, extension):
        print(ctx.author.id)
        if dev.is_developer(ctx.author.id):
            self.bot.unload_extension(extension)
            try:
                self.bot.load_extension(extension)
                await ctx.send(embed=dev.success(
                    f"Extension `{extension}` reloaded!"))
            except Exception as e:
                await ctx.send(embed=dev.error(e))
        else:
            await ctx.send(embed=dev.not_dev())


def setup(bot):
    bot.add_cog(Management(bot))
