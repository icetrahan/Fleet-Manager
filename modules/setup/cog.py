import discord
from discord.ext import commands
from discord.utils import get


class Setup(commands.Cog, name="Safety"):
  """Recieves ticket commands"""
  

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setuprules(self, ctx: commands.Context):
    em = discord.Embed(title = "Fleet DAO Rules", description ="1.  We are not financial advisors. Do your own research. Do not take staffs words as financial advice.\n\n2.  Wear protection.\n\n          2.1: Staff will never ask you for personal information including passwords, addresses, or private keys. Keep an eye out for potential scammers, and if you come across any please report them.\n          2.2: Do not post person information in this Discord. What you do in your private messages is your business. This includes addresses, emails, phone numbers, etc.\n          2.3: Doxing or even the threat of doxing is not allowed.\n\n3. The Golden Rule.\n          3.1: Treat everyone with kindness. Trolling, baiting, shaming, discrimination, slurs, or personal attacks of any sort will not be tolerated.\n          3.2: Racial slurs (no matter the race) will not be tolerated. Be it in jokes, usernames, images, gifs, profile pictures, etc.\n          3.3: NSFW images, gifs, profile pictures, or content of any kind is not allowed.\n\n4. Scam or Spam\n          4.1: Do not post any kind of scam or phishing links, posts, or content. Doing so will result in a ban.\n          4.2: Do not direct message members of this server with links to any servers, websites, ect.\n          4.3: One account per member. If you are caught using multiple accounts, all accounts found will be banned from the server.\n          4.4: Please avoid spam. Keep you messages in the right channels and don't post the same message twice.\n\n5. Mod Discretion.\n          5.1: Moderators are allowed to use their own discretion when dealing with issues in the server. If a mod finds an issue that isn't written in these rules, then that is at their own discretion.\n          5.2: If you have a problem with a moderator do not contact them directly. Please file a report and someone on our mod team (besides that mod) will investigate.",color = 0x00a8ff)
    await ctx.send(embed=em)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setupourteam(self, ctx: commands.Context):
    em = discord.Embed(title = "Fleet Team Member: Icetrahan", description ="Hey Fleet DOA!\n\nI'm Caleb and I can't wait to have you join the Fleet!\n\nI'm a Software Developer/Graphic Designer out of Louisiana. I specialize in mobile apps and mobile games! I actually did all the coding of Fleet Manager myself! When I'm not coding or designing I'm buying up real estate, fishing up the lakes, or hanging out with my little family.\n\nWe're glad to have you here and can't wait to have you in our e-yacht club!")
    em.set_image(url="https://cdn.discordapp.com/avatars/551445344609763338/8e5c924f81f58a23927ceb99b7aa503e.webp?size=128")
    await ctx.send(embed=em)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setuplinks(self, ctx: commands.Context):
    em = discord.Embed(title = "Fleet Official Links", description ="Our Website: https://fleetdao.vip/ \n\nOur Twitter: https://twitter.com/FleetDAO_NFT \n\nOur Instagram: https://www.instagram.com/fleetdao/ \n\nOur Youtube: https://www.youtube.com/channel/UCuHgc5MbmFfiCwJIPgjs0Vw \n\nOur LinkedIn: https://www.linkedin.com/company/fleetdao/?original_referer=https%3A%2F%2Ffleetdao.vip%2F")
    await ctx.send(embed=em)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def setupfaq(self, ctx: commands.Context):
    em = discord.Embed(title = "Fleet FAQs", description ="I've been bad and got a warning. Is this the end?\n\nOf course it's not the end, unless you get 10 warnings (which results in a ban). Once you recieve 3 warnings you will be muted in the server for 30 minutes everytime you recieve a warning. Once you reach 10 total warnings, fare thee well ole chap.\n\n\nI have a question/I want to report someone.\n\nTo ask our admin team a question or to report someone, head over to the support-ticket channel and the prompt there will tell you how to start a ticket!\n\nI feel I was wrongfully warned.\n\nIf you feel you were warned in error or wrongfully warned you can head to the support-ticket channel and the prompt there will tell you how to start a ticket!\n\n\nWhat is Fleet DAO\'s goal?\n\nWorld Domination! Well not exactly, but close! Fleet DAO\'s goal is to have our own fleet of yachts that our members can use! Not only do we want you to hop on board (literally), but we also have much more to offer! Check out our website in the official-links for more on Fleet DAO!\n\n\nWhy can't I post links?\n\nTo help keep our server secure and prevent scams we block all links that are not submited in the marketplace tab. Should you want to sell an NFT (it doesn't just have to be a Fleet DAO NFT) be sure to post it in the marketplace and nowhere else.\n\n\nHow can I become a moderator?\n\nFleet DAO is not currently looking for moderators, however, when we do we will post an announcement in the announcement tab so be sure to have notifications turned on!\n\n\nWhat are the rules of the server?\n\nAll the server rules can be found in the rules channel at the top of the server navigation bar!\n\n\nIf you have any questions that were not answered here, be sure to ask them using our support-ticket channel!")
    await ctx.send(embed=em)
    
def setup(bot: commands.bot):
  bot.add_cog(Setup(bot))