# bot.py
import discord
from discord.ext import commands
import json
import os
from typing import Dict, List, Optional

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

class ServerConfig:
    def __init__(self, config_path: str = "server_config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """Load the configuration from JSON file"""
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
        """Save the current configuration to JSON file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    """Configure the server based on JSON config"""
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
    """Create categories and return a mapping of names to category objects"""
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
    """Create roles from config"""
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
    """Create channels from config with category support"""
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
    """Apply server settings from config"""
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

if __name__ == "__main__":
    bot.run('YOUR_BOT_TOKEN_HERE')