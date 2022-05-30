import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('OTgwODY1NzA0NTIzODU4MDAw.Gx4vMw.6FaQUF3ydBPytwidaihsFPwi6YrA9rD3tD09SU')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

client.run(token)
