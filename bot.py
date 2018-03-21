import discord 
from discord.ext import commands
from discord.voice_client import VoiceClient
import youtube_dl

startup_extensions = ["Music"]
bot = commands.Bot("?")

class Main_Commands():
    def __init__(self,bot):
      self.bot = bot

if __name__ == "__main__":
 for extension in startup_extensions:
   try:
     bot.load_extension(extension)
   except Exception as e:
     exc = '{}: {}'.format(type(e).__name__,e)
     print('Failed to load extension {}\n{}'.format(extension, exc))


bot.run("NDI2MDE1MzAxOTUyMzM5OTY4.DZQBlg.bCwyfXTtRmoHlvw6w8W2xo9OooY")
