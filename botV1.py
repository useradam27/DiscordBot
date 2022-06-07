import discord
import os
import web_scrape
import xur_scrape
import light_scrape

from dotenv import load_dotenv
from os import getenv

load_dotenv()

# instantiate discord client 
client = discord.Client()

web_get = web_scrape.BungieNews()
no_result_message = 'none'

xur_get = xur_scrape.XurNews()
light_get = light_scrape.LightNews()

# discord event to check when the bot is online 
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Type .help for commands"))
  print(f'{client.user} is now online!')
  
@client.event
async def on_message(message):
  if message.author == client.user:
        return
      
  message_content = message.content.lower() 
  
  if message.content.startswith(f'.hello'):
        await message.channel.send("Hello!!!")
        

    
  if f'.twab' in message_content:
    result_links = web_get.search_link()
    links = web_get.send_link(result_links, 1)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.hotfix' in message_content:
    result_links = web_get.search_link()
    links = web_get.send_link(result_links, 2)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.inventory' in message_content:
    result_links = xur_get.search_inventory()
    links = xur_get.send_inventory(result_links)
    
    if len(links) > 0:
      await message.channel.send('Xur\'s inventory this week:')
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.xur' in message_content:
    result_links = xur_get.search_location()
    links = xur_get.send_location(result_links)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
      
  if f'.inventory_detail' in message_content:
    result_links = xur_get.search_inventory()
    links = xur_get.send_inventory(result_links)
    
    if len(links) > 0:
      for link in links:
        r = light_get.search_link(link)
        l = light_get.send_link(r)
        if len(links) > 0:
          for l2 in l:
            await message.channel.send(l2)
        else:
          await message.channel.send(no_result_message)
    else:
      await message.channel.send(no_result_message)
      
  if f'.help' in message_content:
    await message.channel.send("List of commands:\n")
    await message.channel.send(".twab : latest this week at bungie update")
    await message.channel.send(".hotfix : latest destiny 2 hotfix")
    await message.channel.send(".xur : Xur's location for current week")
    await message.channel.send(".inventory : Xur's current inventory")
    await message.channel.send(".inventory_detail : light.gg links for Xur's inventory")

# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))
