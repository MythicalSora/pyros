from helpers.config import Config
import discord


class Dev():
    def __init__(self):
        self.config = Config(
            '/home/michael/programming/python/pyros/config.yml'
        )
        self.config = self.config.read_config()

    def is_developer(self, user):
        for dev in self.config['developers']:
            if dev == user:
                return True
        return False

    def error(self, error):
        return discord.Embed(
            title=":warning: **Error**",
            description=f"{type(error).__name__}:\n ```sh {error}```",
            color=discord.Colour.red()
        )

    def success(self, msg):
        return discord.Embed(
            title=":white_check_mark: **Success!**",
            description=msg,
            color=discord.Colour.green()
        )

    def not_dev(self):
        return discord.Embed(
            title=":octagonal_sign: **Action not permitted.**",
            description="Only developers are allowed to use this command.",
            color=discord.Colour.red()
        )
