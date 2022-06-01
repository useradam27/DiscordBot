import discord
import os
import web_scrape
import xur_scrape

from dotenv import load_dotenv
from os import getenv

load_dotenv()

# instantiate discord client 
client = discord.Client()

web_get = web_scrape.BungieNews()
no_result_message = 'none'

xur_get = xur_scrape.XurNews()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  print(f'{client.user} is now online!')
  
@client.event
async def on_message(message):
  if message.author == client.user:
        return
      
  message_content = message.content.lower() 
  
  if message.content.startswith(f'.hello'):
        await message.channel.send("Hello!!!")
        

    
  if f'.news' in message_content:
    result_links = web_get.search_link()
    links = web_get.send_link(result_links)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.xur_inventory' in message_content:
    result_links = xur_get.search_inventory()
    links = xur_get.send_inventory(result_links)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.xur_location' in message_content:
    result_links = xur_get.search_location()
    links = xur_get.send_location(result_links)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))
