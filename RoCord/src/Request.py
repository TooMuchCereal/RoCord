#---IMPORTS---#

import discord
from discord.ext import commands

import robloxpy
from Message import *

#---BOT IS READY---#

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#--Get A Small Hello From Bot--#

@client.command()
async def Hey(ctx):
      await ctx.send(Welcome.format(ctx.message.author.mention))

#--Get A Groups Info--#    

@client.command()
async def GetGroupInfo(ctx):
    
    Context_Message = ctx.message.content.split(" ")[1]
    
    try:
        Group_Description = robloxpy.Group.External.GetDescription(Context_Message)
        Group_Count = robloxpy.Group.External.GetMemberCount(Context_Message)

        Group_Name = robloxpy.Group.External.GetName(Context_Message)
        Group_Owner = robloxpy.Group.External.GetOwner(Context_Message)



        await ctx.send(Group.format(Group_Name, Group_Owner, Group_Count, Group_Description))    
    except:
        await ctx.send("Sorry Couldnt Get Group Info")
@client.command()
async def GetUserImage(ctx):
    
    Context_Message = ctx.message.content.split(" ")[1]
    
    try:
        Image = robloxpy.User.External.GetHeadshot(Context_Message)
        Embed = discord.embed(title=f'{ctx.author.mention} Has Requested An Image')

        Embed.add_field(name='Content', value=Image, inline=False)
        await ctx.send(embed=Embed)
    except:
        pass
client.run()
