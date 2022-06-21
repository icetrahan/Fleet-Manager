import os
import discord
from discord.ext import commands


def main():
    intents = discord.Intents().all()
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")

    client.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    main()
