from discord.ext import commands
from helpers.anime import get_search_results, query_embed, get_anime
from bs4 import BeautifulSoup
from jikanpy import Jikan

import discord
import requests


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.jikan = Jikan()

    @commands.command()
    async def xkcd(self, ctx: commands.Context):
        res = requests.get("https://c.xkcd.com/random/comic/")
        soup = BeautifulSoup(res.content, features="html.parser")
        comic = soup.find("div", attrs={"id": "comic"}).find("img")

        embed = discord.Embed(
            title=comic["alt"],
            colour=discord.Colour.from_rgb(255, 105, 180),
            url=res.url
        )

        embed.set_image(url=f"https:{comic['src']}")

        await ctx.send(embed=embed)

    @commands.command()
    async def anime(self, ctx: commands.Context, *args):
        animes = get_search_results(' '.join(args[:]))
        embed = query_embed(animes)

        await ctx.send(embed=embed)
        input = await self.bot.wait_for(
            'message',
            check=lambda message: message.author == ctx.author)

        await ctx.send(embed=get_anime(animes, int(input.content)))


def setup(bot):
    bot.add_cog(Fun(bot))
