import json
import os
import re
import urllib.request
import llm
import data

import discord
from dotenv import load_dotenv

TOKEN_ENV_PATH = "env/token.env"
load_dotenv(dotenv_path=TOKEN_ENV_PATH)
TOKEN_NAME = "TOKEN_MAIN"
TOKEN = os.getenv(TOKEN_NAME)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def meningOverJef(message):
    await message.channel.send("Ik haat jef!", reference=message)


async def sendGif(message):
    message_format = message.content.split("_")
    if len(message_format) != 2 or not message_format[1].isdigit():
        return
    await message.channel.send(data.gifs[int(message_format[1])], reference=message)


async def addReaction(message, emoji_name):
    await message.add_reaction(data.emojies[emoji_name])


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
    f"{data.BOT_TAG} mening over jef?": meningOverJef,
    data.BOT_TAG: botTag,
    f"{data.BOT_TAG} tell a joke": tellAJoke,
}
for i in range(0, len(data.gifs)):
    commands_full[f"gif_{i}"] = sendGif


async def profEmojiReact(message):
    for prof in data.prof_to_emoji:
        if re.match(prof.regex, message.content):
            await addReaction(message, prof.emoji)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print()
    print(message.author)
    print(message.content)
    used_command = False

    if (
        TOKEN_NAME == "TOKEN_MAIN"
        and message.channel.id == data.LENNERD_TEST_CHANNEL_ID
    ):
        return

    if message.author == client.user:
        return

    if message.content in commands_full:
        used_command = True
        await commands_full[message.content](message)

    # for command in commands_partial:
    #     await command(message)

    if not used_command and message.content.startswith(data.BOT_TAG):
        await llm.askLLM(message)


if TOKEN is not None:
    client.run(TOKEN)
else:
    print(f"Invalid token:${TOKEN}")
