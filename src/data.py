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

gifs = [
    "https://tenor.com/view/roblox-funny-roblox-suit-roblox-tux-roblox-meme-gif-15378536397008769771",
    "https://tenor.com/view/gracias-por-su-atencion-gif-con-movimiento-para-power-point-triste-gif-15976180513104321087",
    "https://tenor.com/view/cat-reaction-michi-triste-crying-cat-reaction-sad-cat-hannicion-gif-17190162121303461099",
    "https://media.discordapp.net/attachments/1009877926336008293/1026965859467542569/t-1.gif?ex=68df943d&is=68de42bd&hm=6d4a2b3730bdc89c1eee4e47442f4ac861f67521ed7e54fef4d383c5c795323a&",
    "https://tenor.com/view/cringe-gif-24107071",
]


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
