import os
import discord

from discord import Intents, Embed
from keys import discord_api_key

# ---  Intents  ---
intents = Intents.default()
intents.message_content = True   # Needed to read message text
intents.members = True           # Needed for joined_at & roles

# ---  Client  ---
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (id: {client.user.id})")

@client.event
async def on_message(message: discord.Message):
    # Ignore the bot's own messages / other bots
    if message.author.bot:
        return

    # 1) Print to console
    print(f"[#{message.channel}] {message.author} ({message.author.id}): {message.content}")

    # 2) Build user details
    user = message.author  # discord.Member in guilds, discord.User in DMs
    member = user if isinstance(user, discord.Member) else None

    # If in a server and not a Member object yet, try to fetch it for more details
    if message.guild and member is None:
        try:
            member = await message.guild.fetch_member(user.id)
        except discord.NotFound:
            member = None

    # Prepare fields
    display_name = getattr(user, "display_name", user.name)
    global_name = getattr(user, "global_name", None)
    created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")

    joined = "Unknown"
    roles_text = "None"
    if member:
        if member.joined_at:
            joined = member.joined_at.strftime("%Y-%m-%d %H:%M:%S UTC")
        role_mentions = [r.mention for r in member.roles if r.name != "@everyone"]
        roles_text = ", ".join(role_mentions) if role_mentions else "None"

    # 3) Send an embed with details + the message they sent
    embed = Embed(title="User details", description=f"**Message:** {message.content}")
    
    # Thumbnail = user's avatar
    embed.set_thumbnail(url=user.display_avatar.url)

    # If the user attached an image, show it as the main image
    img = next(
        (a for a in message.attachments
         if (a.content_type or "").startswith("image/")
         or a.filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"))),
        None
    )
    if img:
        embed.set_image(url=img.url)
    
    embed.set_author(name=f"{user} • ID: {user.id}", icon_url=user.display_avatar.url)
    embed.add_field(name="Display name", value=display_name, inline=True)
    embed.add_field(name="Global name", value=global_name or "—", inline=True)
    embed.add_field(name="Bot account?", value=str(user.bot), inline=True)
    embed.add_field(name="Account created", value=created_at, inline=True)
    if message.guild:
        embed.add_field(name="Joined this server", value=joined, inline=True)
        embed.add_field(name="Roles", value=roles_text, inline=False)

    await message.channel.send(embed=embed)

# ---  Run  --- #
token = discord_api_key
if not token:
    raise SystemExit("Please set the DISCORD_TOKEN environment variable to your bot token.")
client.run(token)
