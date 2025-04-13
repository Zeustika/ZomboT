import discord
import asyncio
import os
from rcon.source import Client
from dotenv import load_dotenv

# Load variabel dari .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
RCON_HOST = os.getenv("RCON_HOST")
RCON_PORT = int(os.getenv("RCON_PORT"))
RCON_PASSWORD = os.getenv("RCON_PASSWORD")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL"))

# Inisialisasi bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

# Fungsi untuk cek jumlah pemain di server
async def get_player_count():
    try:
        with Client(RCON_HOST, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run("players")

            if response:
                lines = response.strip().split("\n")  # Hapus whitespace dan pecah per baris

                # Pastikan ada baris kedua (nama pemain)
                if len(lines) > 1:
                    player_list = [p.strip() for p in lines[1:] if p.strip()]
                    player_count = len(player_list)
                else:
                    player_count = 0  # Tidak ada pemain online
                
                return player_count
    except Exception as e:
        print(f"Error RCON: {e}")
        return None


# Task untuk update status bot secara berkala
async def update_status():
    await bot.wait_until_ready()
    while not bot.is_closed():
        player_count = await get_player_count()
        if player_count is not None:
            status = f"{player_count}/10 players online" if player_count > 0 else "No players online"
            activity = discord.Activity(type=discord.ActivityType.watching, name=status)
            await bot.change_presence(activity=activity)
        await asyncio.sleep(UPDATE_INTERVAL)


# Event saat bot siap
@bot.event
async def on_ready():
    print(f"Bot {bot.user} sudah online!")
    bot.loop.create_task(update_status())

# Jalankan bot
bot.run(DISCORD_TOKEN)
