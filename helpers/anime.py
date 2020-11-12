from jikanpy import Jikan
import discord

jikan = Jikan()


def get_anime(animes, index):
    i = 1
    for anime in animes:
        if i == index:
            return anime_embed(jikan.anime(anime.get('mal_id')))

        i += 1


def anime_embed(anime):
    embed = discord.Embed(
        title=anime.get('title'),
        colour=discord.Colour.green(),
        url=anime.get('url'),
        description=anime.get('synopsis')
    )

    embed.set_thumbnail(url=anime.get('image_url'))
    embed.add_field(
        name=":hourglass: **Status**",
        value=anime.get('status')
    )
    embed.add_field(
        name=":triangular_flag_on_post:**Rating**",
        value=anime.get("rating")
    )
    embed.add_field(
        name=":star: **Score**",
        value=anime.get("score")
    )
    embed.add_field(
        name=":desktop: **Studio**",
        value=anime.get('studios')[0].get('name'),
        inline=True
    )
    embed.add_field(
        name=":video_camera: **Episodes**",
        value=anime.get('episodes')
    ),
    embed.add_field(
        name=":mag: **Type**",
        value=anime.get('type')
    )

    return embed


def get_search_results(query):
    results = []
    index = 1

    for result in jikan.search('anime', query).get("results"):
        if index > 10:
            break
        else:
            results.append(result)
            index += 1

    return results


def query_embed(animes):
    index = 1
    desc = ''

    for anime in animes:
        desc += f"**{index}. [{anime.get('title')}]({anime.get('url')})**\n"
        index += 1

    embed = discord.Embed(
        title="Reply with the number you want to select",
        color=discord.Colour.blue(),
        description=desc
    )

    return embed
