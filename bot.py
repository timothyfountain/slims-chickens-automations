
import os
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
BOT_STATUS = os.getenv("BOT_STATUS", "Managing Slims Chickens.")
STATUS_TYPE = os.getenv("STATUS_TYPE", "custom").lower()

ACTIVITY_TYPES = {
    "playing": discord.ActivityType.playing,
    "watching": discord.ActivityType.watching,
    "listening": discord.ActivityType.listening,
    "competing": discord.ActivityType.competing,
}


class PresenceBot(discord.Client):
    async def on_ready(self):
        activity_type = ACTIVITY_TYPES.get(
            STATUS_TYPE,
            discord.ActivityType.playing
        )

        activity = discord.Activity(
            type=activity_type,
            name=BOT_STATUS
        )

        await self.change_presence(
            status=discord.Status.online,
            activity=activity
        )

        print(f"logged in as {self.user}")
        print(f"activity: {STATUS_TYPE} {BOT_STATUS}")


if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing!")

intents = discord.Intents.default()

client = PresenceBot(intents=intents)
client.run(TOKEN)
