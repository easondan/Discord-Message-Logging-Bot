import discord
import requests
from discord.ext import commands
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
  print("logged in as Student Bot")
  print(client.user.name)
  print(client.user.id)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Student"))




@client.event
async def on_message(message):
#use this message to prevent the bot from recursively send messages
  if message.author == client.user:
    return
  author = message.author
  content = message.content
  channel = message.channel
  id = message.id
  channel2 = client.get_channel(insert discord channel id)
  f = open("messages.txt", "a")
  f.write("{} {} {} {}\n".format(id,author,content,channel))
  await channel2.send('\n-------------------\nUser: {}  \nContent: "{}"  \nChannel: {}'.format(author,content,channel))
  await client.process_commands(message)




@client.event
async def on_message_delete(message):
  author = message.author
  content = message.content
  channel = message.channel
  id = message.id
  channel2 = client.get_channel(insert discord channel id)
  f = open("deleteMessage.txt", "a")
  f.write("{} {} {} {}\n".format(id,author,content,channel))
  await channel2.send('\n-------------------\nDeleted message: \nUser: {}  \nContent: "{}"  \nChannel: {}'.format(author,content,channel))



@client.event 
async def on_message_edit(before,after):
  author = before.author
  id = before.id
  content_before = before.content
  content_after = after.content
  channel = before.channel
  channel2 = client.get_channel(insert discord channel id)
  f = open("editMessage.txt", "a")
  f.write("{} {} {} {} {}\n".format(id,author,content_before,content_after,channel))
  await channel2.send('\n-------------------\nEdit Message: \nUser: {} \n Before: "{}" \n After: "{}" \n Channel:{}'.format(author,content_before,content_after,channel))
  

keep_alive()
client.run(os.getenv('TOKEN'))




