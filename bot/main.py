# bot.py
import json
import os
from typing import Dict, List, Optional

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


def get_token(api_token: str) -> str:
    """Returns the requested API token

    Args:
        api_token (str): Identifies which API token to return
    
    TODO:
        Need a more secure solution for API tokens than storing them in the environment

    Returns:
        str: The requested API token
    """    
    token = os.getenv(api_token)
    if token:
        return token


""" class ServerConfig:
    def __init__(self, config_path: str = "server_config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict:
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "roles": [],
                "categories": [],
                "channels": {
                    "text": [],
                    "voice": []
                },
                "settings": {}
            }

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4) """

@bot.event
async def on_ready():
    """ on_ready event handler

    Execute any code that has to wait until the bot is connected to the Discord server (guild). For now, the bot is 
    just letting us know it's connected by displaying the server name.

    TODO:
        * Remove this code and replace it with useful business logic
    """
    guild = discord.utils.find(lambda g: g.name == os.getenv("DISCORD_GUILD"), bot.guilds)
    print(f'Bot connected as {bot.user} to {guild}')


@bot.event
async def on_message(message: discord.Message):
    """on_message event handler

     For now just display some message attributes of messages sent to the bot.

    Args:
        message (discord.Message): an instance of a Discord message object
    """
    print(f'Message from {message.author}: {message.content}')


"""@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    config = ServerConfig()
    
    try:
        # Create categories first
        category_map = await create_categories(ctx.guild, config.config["categories"])
        
        # Create roles
        await create_roles(ctx.guild, config.config["roles"])
        
        # Create channels with category references
        await create_channels(ctx.guild, config.config["channels"], category_map)
        
        # Apply server settings
        await apply_settings(ctx.guild, config.config["settings"])
        
        await ctx.send("Server configuration completed successfully!")
    except Exception as e:
        await ctx.send(f"Error during setup: {str(e)}")

async def create_categories(guild: discord.Guild, categories: List[Dict]) -> Dict[str, discord.CategoryChannel]:
    category_map = {}
    existing_categories = {cat.name.lower(): cat for cat in guild.categories}
    
    for cat_config in categories:
        if cat_config["name"].lower() not in existing_categories:
            category = await guild.create_category(
                name=cat_config["name"],
                position=cat_config.get("position", 0),
                overwrites=cat_config.get("overwrites", {})
            )
            category_map[cat_config["name"]] = category
        else:
            category_map[cat_config["name"]] = existing_categories[cat_config["name"].lower()]
    
    return category_map

async def create_roles(guild: discord.Guild, roles: List[Dict]):
    existing_roles = {role.name.lower(): role for role in guild.roles}
    
    for role_config in roles:
        if role_config["name"].lower() not in existing_roles:
            await guild.create_role(
                name=role_config["name"],
                color=discord.Color(int(role_config.get("color", "0x000000").replace("#", ""), 16)),
                permissions=discord.Permissions(permissions=role_config.get("permissions", 0)),
                hoist=role_config.get("hoist", False),
                mentionable=role_config.get("mentionable", False)
            )

async def create_channels(guild: discord.Guild, channels: Dict, category_map: Dict[str, discord.CategoryChannel]):
    # Create text channels
    for channel_config in channels.get("text", []):
        category = category_map.get(channel_config.get("category")) if channel_config.get("category") else None
        await guild.create_text_channel(
            name=channel_config["name"],
            category=category,
            topic=channel_config.get("topic"),
            position=channel_config.get("position", 0),
            overwrites=channel_config.get("overwrites", {})
        )

    # Create voice channels
    for channel_config in channels.get("voice", []):
        category = category_map.get(channel_config.get("category")) if channel_config.get("category") else None
        await guild.create_voice_channel(
            name=channel_config["name"],
            category=category,
            bitrate=channel_config.get("bitrate", 64000),
            user_limit=channel_config.get("user_limit", 0),
            position=channel_config.get("position", 0),
            overwrites=channel_config.get("overwrites", {})
        )

async def apply_settings(guild: discord.Guild, settings: Dict):
    if "name" in settings:
        await guild.edit(name=settings["name"])
    if "description" in settings:
        await guild.edit(description=settings["description"])

@setup.error
async def setup_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need administrator permissions to use this command!")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

 """

if __name__ == "__main__":
    bot.run(get_token('DISCORD_TOKEN'))