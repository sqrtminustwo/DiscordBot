import os
from dotenv import load_dotenv
import discord

TOKEN_ENV_PATH = "env/token.env"
load_dotenv(dotenv_path=TOKEN_ENV_PATH)
TOKEN = os.getenv("TOKEN")
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
BOT_TAG = "<@1423047868876587039>"


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(message)
    print(message.content)

    if message.author == client.user:
        return

    if message.content == "mening over jef?":
        await message.channel.send("Ik haat jef!")

    if BOT_TAG in message.content:
        await message.add_reaction("<:jef_opp:1423005081003102269>")


if TOKEN is not None:
    client.run(TOKEN)
else:
    print(f"Invalid token:${TOKEN}")
