import discord
from discord.ext import commands
from commands import greet_user, add_numbers

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def greet(ctx, name: str):
    response = await greet_user(name)
    await ctx.send(response)

@bot.command()
async def add(ctx, a: int, b: int):
    result = await add_numbers(a, b)
    await ctx.send(f"Result: {result}")

bot.run("YOUR_TOKEN")