import discord
from discord.ext import tasks
from discord.ext import commands
from discord.utils import get
import json
import asyncio


with open('./stats.json', 'r') as f:
  stats = json.load(f)

with open('./warns.json', 'r') as j:
  warns = json.load(j)


class Stats(commands.Cog, name="Safety"):
  """Recieves stats commands"""
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    self.server_stats.start()
  
  @tasks.loop(seconds = 60)
  async def server_stats(self):
    bot=self.bot

    with open('./warns.json', 'r') as j:
      warns = json.load(j)
    
    guild = bot.get_guild(978840408979296286)

    ## Stat Values
    memberCount=len(set(bot.get_all_members()))
    
    aRole=get(guild.roles, id=978847278041301032)
    mRole=get(guild.roles, id=984720439731449856)
    mList=[]
    for user in aRole.members:
      if str(user.status)=="online":
        mList.append(user)
    await asyncio.sleep(1)
    for user in mRole.members:
      if str(user.status)=="online":
        mList.append(user)
        
    modCount=len(mList)
    
    banCount=stats["Bans"]

    warnCount=0
    for k,v in warns.items():
      warnCount += int(warns[k]["warningsCount"])

    ## Stat Channels
    memberCountCh=bot.get_channel(int(stats["Channels"]["MemberVC"]))
    await asyncio.sleep(1)
    modCountCh=bot.get_channel(int(stats["Channels"]["ModsOnlineVC"]))
    await asyncio.sleep(1)
    banCountCh=bot.get_channel(int(stats["Channels"]["BansVC"]))
    await asyncio.sleep(1)
    warnCountCh=bot.get_channel(int(stats["Channels"]["WarningsVC"]))
    await asyncio.sleep(1)

    print("here now")

    ##Change Channel Names
    await memberCountCh.edit(name= f"Members: {memberCount}")
    await asyncio.sleep(1)
    await modCountCh.edit(name= f"Moderators Online: {modCount}")
    await asyncio.sleep(1)
    await banCountCh.edit(name= f"Bans: {banCount}")
    await asyncio.sleep(1)
    await warnCountCh.edit(name= f"Warnings Issued: {warnCount}")
    print('at the end')
    

  
def setup(bot: commands.Bot):
  bot.add_cog(Stats(bot))