
import os
import discord

from dotenv import load_dotenv

# load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
BOT_STATUS = os.getenv(
    "BOT_STATUS",
    "Managing Slims Chickens."
)
STATUS_TYPE = os.getenv("STATUS_TYPE", "custom").lower()

# supported activity types
ACTIVITY_TYPES = {
    "playing": discord.ActivityType.playing,
    "watching": discord.ActivityType.watching,
    "listening": discord.ActivityType.listening,
    "competing": discord.ActivityType.competing,
}


class PresenceBot(discord.Client):

    async def on_ready(self):
        print("--------------------------------")
        print(f"logged in as: {self.user}")
        print(f"bot id: {self.user.id}")
        print("--------------------------------")

        # create activity
        if STATUS_TYPE == "custom":
            activity = discord.CustomActivity(
                name=BOT_STATUS
            )

        else:
            activity_type = ACTIVITY_TYPES.get(
                STATUS_TYPE,
                discord.ActivityType.playing
            )

            activity = discord.Activity(
                type=activity_type,
                name=BOT_STATUS
            )

        # update presence
        await self.change_presence(
            status=discord.Status.online,
            activity=activity
        )

        print(f"status type: {STATUS_TYPE}")
        print(f"status text: {BOT_STATUS}")
        print("presence successfully updated!")


# validate token
if not TOKEN:
    raise ValueError(
        "DISCORD_TOKEN is missing from your .env file!"
    )


# initialize bot
intents = discord.Intents.default()

client = PresenceBot(
    intents=intents
)

# start bot
client.run(TOKEN)
