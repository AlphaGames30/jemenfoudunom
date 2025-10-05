import discord
from discord.ext import commands
from app import socketio  # On importera le serveur Flask

TOKEN = "VOTRE_BOT_TOKEN"  # Remplace par ton token bot

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} connecté!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Émettre le message au serveur Flask via SocketIO
    socketio.emit('new_message', {
        'user': str(message.author),
        'content': message.content,
        'channel': str(message.channel)
    })
