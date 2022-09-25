#MTAyMTA0MzcwODU5MTg3NDE0OQ.GaUpGb.Kev6s07dky7_d6l-nASiZ-Ijq3N9nFqQsQIMik
import discord
from discord.ext import commands

config = {
    'token': 'MTAyMTA0MzcwODU5MTg3NDE0OQ.GaUpGb.Kev6s07dky7_d6l-nASiZ-Ijq3N9nFqQsQIMik',
    '#': '#',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)

bot.run(config['token'])