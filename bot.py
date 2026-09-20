import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def roles(ctx):
    embed = discord.Embed(title="Server Roles", color=0x5865F2)
    embed.add_field(name="Roles", value="Team Member\nBuilder\nTrader\nResearcher\nJust Browsing\nServer Booster", inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
