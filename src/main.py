import json
import os
import urllib.request
import discord
from dotenv import load_dotenv
import re

TOKEN_ENV_PATH = "env/token.env"
load_dotenv(dotenv_path=TOKEN_ENV_PATH)
TOKEN_NAME = "TOKEN_MAIN"
TOKEN = os.getenv(TOKEN_NAME)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
BOT_TAG = "<@1423047868876587039>"
LENNERD_TEST_CHANNEL_ID = 1423277829654712462
emojies = {
    "jef_opp": "<:jef_opp:1423005081003102269>",
    "gunnar": "<:gunnar:1423004268486459492>",
    "andy": "<:andy:1423004045706006709>",
    "georgi": "<:georgi:1423270976619020449>",
    "oliver": "<:oliver:1423004640961757204>",
    "filip": "<:filip:1423951861362196630>",
}


async def meningOverJef(message):
    await message.channel.send("Ik haat jef!", reference=message)


gifs = [
    "https://tenor.com/view/roblox-funny-roblox-suit-roblox-tux-roblox-meme-gif-15378536397008769771",
    "https://tenor.com/view/gracias-por-su-atencion-gif-con-movimiento-para-power-point-triste-gif-15976180513104321087",
    "https://tenor.com/view/cat-reaction-michi-triste-crying-cat-reaction-sad-cat-hannicion-gif-17190162121303461099",
    "https://media.discordapp.net/attachments/1009877926336008293/1026965859467542569/t-1.gif?ex=68df943d&is=68de42bd&hm=6d4a2b3730bdc89c1eee4e47442f4ac861f67521ed7e54fef4d383c5c795323a&",
    "https://tenor.com/view/cringe-gif-24107071",
]


async def sendGif(message):
    message_format = message.content.split("_")
    if len(message_format) != 2 or not message_format[1].isdigit():
        return
    await message.channel.send(gifs[int(message_format[1])], reference=message)


async def addReaction(message, emoji_name):
    await message.add_reaction(emojies[emoji_name])


async def botTag(message):
    await addReaction(message, "jef_opp")


async def tellAJoke(message):
    with urllib.request.urlopen(
        "https://official-joke-api.appspot.com/random_joke"
    ) as url:
        data = json.loads(url.read().decode())
        setup_message = await message.channel.send(data["setup"], reference=message)

        def wait_to_send_punchline(m):
            return (
                m.channel == message.channel
                and m.reference is not None
                and m.reference.message_id == setup_message.id
            )

        try:
            ask_for_punchline = await client.wait_for(
                "message", check=wait_to_send_punchline, timeout=15
            )
            await message.channel.send(data["punchline"], reference=ask_for_punchline)
        except TimeoutError:
            await message.channel.send(
                "Why ask for a joke if you don't want to hear the punchline...",
                reference=message,
            )


# full message should match
commands_full = {
    f"{BOT_TAG} mening over jef?": meningOverJef,
    BOT_TAG: botTag,
    f"{BOT_TAG} tell a joke": tellAJoke,
}
for i in range(0, len(gifs)):
    commands_full[f"gif_{i}"] = sendGif


class Prof:
    def __init__(self, regex, emoji):
        self.regex = regex
        self.emoji = emoji


prof_to_emoji = [
    Prof("^.*(christophe|scholliers|funcprog|haskell).*$", "jef_opp"),
    Prof("^.*(gunnar|ad|ad2).*$", "gunnar"),
    Prof("^.*(andy|comnet).*$", "andy"),
    Prof("^.*(georgi|stat|statistiek).*$", "georgi"),
    Prof("^.*(oliver|stat|statistiek).*$", "oliver"),
    Prof("^.*(filip|sysprog).*$", "filip"),
]


async def profEmojiReact(message):
    for prof in prof_to_emoji:
        if re.match(prof.regex, message.content):
            await addReaction(message, prof.emoji)


# message should pass the regex
commands_partial = [profEmojiReact]


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

    if message.content in commands_full:
        await commands_full[message.content](message)

    for command in commands_partial:
        await command(message)


if TOKEN is not None:
    client.run(TOKEN)
else:
    print(f"Invalid token:${TOKEN}")
