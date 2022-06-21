import discord
from discord.ext import commands
from discord.utils import get
import json

with open('./warns.json', 'r') as f:
  warns= json.load(f)


def save_warn(ctx, member: discord.Member,reason):
    with open('./warns.json', 'r') as f:
        warns = json.load(f)
        warncount=warns[str(member.id)]["warningsCount"]
        warns[str(member.id)]["warningsCount"]=str(int(warncount)+1)
        warns[str(member.id)]["warnings"][str(int(warncount)+1)]=str("Reason: "+reason),str("By: "+str(ctx.author))
      

    with open('./warns.json', 'w') as f:
         json.dump(warns, f,indent = 2)
    return warns[str(member.id)]["warningsCount"]

def remove_warn(ctx, member: discord.Member, warnNum: int):
    with open('./warns.json', 'r') as f:
        warns = json.load(f)
        warncount=warns[str(member.id)]["warningsCount"]
        warns[str(member.id)]["warningsCount"]=str(int(warncount)-1)
        warns[str(member.id)]["warnings"].pop(str(warnNum))

    with open('./warns.json', 'w') as f:
         json.dump(warns, f,indent = 2)
    

class Safety(commands.Cog, name="Safety"):
  """Recieves warn commands"""
  

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def updatewarnsheet(self,ctx: commands.Context):
    guild = self.bot.get_guild(978840408979296286)
    for member in guild.members:
      for user, data in warns.items():
        if user == member.id:
          found=True
          break
        else:
          found=False
      if not found:
        warns[str(member.id)]={
          "warningsCount" : "0",
          "warnings":
          {
            
          }
        }
      else:
        continue
    await self.bot.message.delete()
    with open('./warns.json','w') as f:
      json.dump(warns,f,indent = 2)
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def warn(self, ctx: commands.Context, member: discord.Member, *, reason):
        warnCount= save_warn(ctx, member,reason)
        em=discord.Embed(title="Warning", description=f"User: {member}\nReason: {reason}\nTotal Warnings: {warnCount}")
        await ctx.message.delete()
        await ctx.send(embed=em)
        guild = self.bot.get_guild(978840408979296286)
        mute= get(guild.roles, id=985251493265432646)
        if int(warnCount)>=10:
          await member.ban()
          with open('./stats.json', 'r') as f:
            stats = json.load(f)
          stats["Bans"]=int(stats["Bans"])+1
          with open('./stats.json', 'w') as f:
            stats = json.dump(f)
            
        elif int(warnCount) in range(3,9):
          await member.add_roles(mute)
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def warnings(self, ctx: commands.Context, member: discord.Member):
        with open('./warns.json', 'r') as f:
          warns = json.load(f)
    
        warnCount=warns[str(member.id)]["warningsCount"]
        warnList=[]
        if int(warns[str(member.id)]["warningsCount"])>=1:
          for warnNumber, warning in warns[str(member.id)]["warnings"].items():
            tempStr=f"Warning Number: {warnNumber}\n"
            for value in warning:
              tempStr=str(tempStr)+value+" \n"
            warnList.append(tempStr)
          fWarnList= "\n".join(warnList)
          em=discord.Embed(title=f"{member.name}\'s Warnings", description=f"Total Warnings: {warnCount} \n\n{fWarnList}")
        else:
          em=discord.Embed(title=f"{member.name}\'s Warnings", description=f"This user has {warnCount} warnings")
        await ctx.send(embed=em)
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def rmwarn(self, ctx: commands.Context, member: discord.Member, warnNum: int):
        remove_warn(ctx, member, warnNum)
        await ctx.send(f"Removed warning {warnNum} from {member.name}.")


def setup(bot: commands.bot):
  bot.add_cog(Safety(bot))