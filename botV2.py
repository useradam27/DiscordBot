import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')
    
bot.run('OTgwODY1NzA0NTIzODU4MDAw.Gx4vMw.6FaQUF3ydBPytwidaihsFPwi6YrA9rD3tD09SU')