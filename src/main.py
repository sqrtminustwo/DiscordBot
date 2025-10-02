import os
from dotenv import load_dotenv
import discord

TOKEN_ENV_PATH = "env/token.env"
load_dotenv(dotenv_path=TOKEN_ENV_PATH)
TOKEN_NAME = "TOKEN_MAIN"
TOKEN = os.getenv(TOKEN_NAME)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
BOT_TAG = "<@1423047868876587039>"
LENNERD_TEST_CHANNEL_ID = 1423277829654712462


async def mening_over_jef(message):
    await message.channel.send("Ik haat jef!")


gifs = [
    "https://tenor.com/view/roblox-funny-roblox-suit-roblox-tux-roblox-meme-gif-15378536397008769771",
    "https://tenor.com/view/gracias-por-su-atencion-gif-con-movimiento-para-power-point-triste-gif-15976180513104321087",
    "https://tenor.com/view/cat-reaction-michi-triste-crying-cat-reaction-sad-cat-hannicion-gif-17190162121303461099",
    "https://media.discordapp.net/attachments/1009877926336008293/1026965859467542569/t-1.gif?ex=68df943d&is=68de42bd&hm=6d4a2b3730bdc89c1eee4e47442f4ac861f67521ed7e54fef4d383c5c795323a&",
    "https://tenor.com/view/cringe-gif-24107071",
]


async def send_gif(message):
    message_format = message.content.split("_")
    if len(message_format) != 2 or not message_format[1].isdigit():
        return
    await message.channel.send(gifs[int(message_format[1])])


async def bot_tag(message):
    await message.add_reaction("<:jef_opp:1423005081003102269>")


commands = {"mening over jef?": mening_over_jef, BOT_TAG: bot_tag}
for i in range(0, len(gifs)):
    commands[f"gif_{i}"] = send_gif


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(message.content)

    if TOKEN_NAME == "TOKEN_MAIN" and message.channel.id == LENNERD_TEST_CHANNEL_ID:
        return

    if message.author == client.user:
        return

    if message.content in commands:
        await commands[message.content](message)


if TOKEN is not None:
    client.run(TOKEN)
else:
    print(f"Invalid token:${TOKEN}")
