from discord.ext import commands
from helpers.config import Config

import discord

config = Config("./config.yml")
config = config.read_config()

intents = discord.Intents.default()
intents.members = True

extensions = [
    "extensions.fun",
    "extensions.management",
    "extensions.moderator"
    ]
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)


@bot.event
async def on_ready():
    print("Currently logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("========================")

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {type(e).__name__} \n {e}")

bot.run(config['token'])
