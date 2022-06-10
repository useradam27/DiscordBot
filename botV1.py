import discord
import os
import bungie_scrape
import xur_scrape
import light_scrape

from dotenv import load_dotenv
from os import getenv

load_dotenv()

#instantiate discord client 
client = discord.Client()

web_get = bungie_scrape.BungieNews()

xur_get = xur_scrape.XurNews()
light_get = light_scrape.LightNews()

#update bot status
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Type .help for commands"))

#main input event  
@client.event
async def on_input(input):
  if input.author == client.user:
        return
   
  #change input to lowercase    
  input_content = input.content.lower() 
  
  
  if input.content.startswith(f'.hello'):
        await input.channel.send("Hello!!!")
        

  #searches bungie news website for twab or hotfix update  
  if f'.twab' in input_content:
    results = web_get.search_link()
    links = web_get.send_link(results, 1)
    
    if len(links) > 0:
      for link in links:
       await input.channel.send(link)
    else:
      await input.channel.send('no results')
      
  if f'.hotfix' in input_content:
    results = web_get.search_link()
    links = web_get.send_link(results, 2)
    
    if len(links) > 0:
      for link in links:
       await input.channel.send(link)
    else:
      await input.channel.send('no results')


  #search whereisxur.com for xur's inventory    
  if f'.inventory' in input_content:
    results = xur_get.search_inventory()
    links = xur_get.send_inventory(results)
    
    if len(links) > 0:
      await input.channel.send('Xur\'s inventory this week:')
      for link in links:
       await input.channel.send(link)
    else:
      await input.channel.send('no results')
   
  #search whereisxur.com for xur's location       
  if f'.xur' in input_content:
    results = xur_get.search_location()
    links = xur_get.send_location(results)
    
    if len(links) > 0:
      for link in links:
       await input.channel.send(link)
    else:
      await input.channel.send('no results')
  
  #provides light.gg links for all of xur's current inventory    
  if f'.inventory_detail' in input_content:
        
    #gets items in xur's inventory
    results = xur_get.search_inventory()
    inv = xur_get.send_inventory(results)
    
    if len(inv) > 0:
      #for every item, get light.gg link
      for item in inv:
        res = light_get.search_link(item)
        item_links = light_get.send_link(res)
        #post links
        if len(item_links) > 0:
          for i in item_links:
            await input.channel.send(i)
        else:
          await input.channel.send('no results')
    else:
      await input.channel.send('no results')
  
  #outputs all comments    
  if f'.help' in input_content:
    await input.channel.send("List of commands:\n")
    await input.channel.send(".twab : latest this week at bungie update")
    await input.channel.send(".hotfix : latest destiny 2 hotfix")
    await input.channel.send(".xur : Xur's location for current week")
    await input.channel.send(".inventory : Xur's current inventory")
    await input.channel.send(".inventory_detail : light.gg links for Xur's inventory")

#get token and run client
client.run(os.getenv('TOKEN'))
