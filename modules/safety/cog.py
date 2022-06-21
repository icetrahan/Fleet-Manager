import discord
from discord.ext import commands
from discord.utils import get
import json
import asyncio


with open('./warns.json', 'r') as f:
  warns = json.load(f)


class Safety(commands.Cog, name="Safety"):
  """Recieves ticket commands"""
  

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    for user, data in warns.items():
      if user == member.id:
        return
      else:
          warns[str(member.id)]={
          "warningsCount" : "0",
          "warnings":
          {
            
          }
        }
    with open('./warns.json', 'w') as f:
      json.dump(warns, f, indent = 2)
  
  @commands.Cog.listener()
  async def on_member_update(self, before, after):
    print(str(after))
    found=False
    if [i.id for i in before.roles].count(978847278041301032):
      for i in after.roles:
        if i == 978847278041301032:
          found=True
          break
        else:
          found==False
      if found:
        return
      else:
        role = before.guild.get_role(978847278041301032)
        await after.add_roles(role)

    if [i.id for i in after.roles].count(985251493265432646):
      ##30 minutes == 1800
      await asyncio.sleep(1800)
      mute= before.guild.get_role(985251493265432646)
      await after.remove_roles(mute)

  @commands.Cog.listener()
  async def on_message(self, message):
    channel= message.channel
    user=message.author
    test_list = ['.com', '.ru', '.net', '.org', '.info', '.biz', '.io', '.co', "https://", "http://"]

    ################### MUTED ROLE#######################
    if [i.id for i in user.roles].count(985251493265432646):
      await message.delete()

    ################## LINK AND SCAM FILTER ##############
    if channel.id == 984717289079337051:
      return
      ##allow admin roles
    elif [i.id for i in user.roles].count(978847278041301032):
      return
    else:
      link_matches = [ele for ele in test_list if(ele in message.content)]
  
      if link_matches:
        await message.delete()
        await channel.send(f"{user.mention} please refrain from posting links unless it is in marketplace or content containing possible scam material. You have been issued a warning. If you have any questions or concerns please open a ticket.")
        with open('./warns.json', 'r') as f:
          warns = json.load(f)

        warncount=warns[str(user.id)]["warningsCount"]
        warns[str(user.id)]["warningsCount"]=str(int(warncount)+1)
        warns[str(user.id)]["warnings"][str(int(warncount)+1)]=str("Reason: Unsafe Material in Message"),str("By: Fleet Manager")

        with open('./warns.json', 'w') as f:
         json.dump(warns, f,indent = 2)

        em=discord.Embed(title="Warning", description=f"User: {user}\nReason: Unsafe Material in Message\nTotal Warnings: {warncount}")
        await channel.send(embed=em)
        guild = self.bot.get_guild(978840408979296286)
        mute= get(guild.roles, id=985251493265432646)
        if int(warncount)>=10:
          await user.ban()
          with open('./stats.json', 'r') as f:
            stats = json.load(f)
          stats["Bans"]=int(stats["Bans"])+1
          with open('./stats.json', 'w') as f:
            stats = json.dump(f)
            
        elif int(warncount) in range(3,9):
          await user.add_roles(mute)
          

def setup(bot: commands.bot):
  bot.add_cog(Safety(bot))