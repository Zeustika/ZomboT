# ZomboT-Discord Player Counter for Project Zomboid

A simple and lightweight Discord bot that connects to your **Project Zomboid server** using RCON and displays the number of online players as its Discord status.

## Features

* Real-time player count display in the bot's status
* Automatically updates at a custom interval
* Uses `discord.py`, `python-dotenv`, and `rcon` libraries

## Requirements

* Python 3.8+
* A running Project Zomboid server with RCON enabled
* A Discord bot token
* RCON host IP, port, and password

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Zeustika/ZomboT.git
cd discord-pz-rcon-bot
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure your environment variables:**

Create a `.env` file based on the provided `.env.example`:

```env
DISCORD_TOKEN=your_discord_token
RCON_HOST=your_server_ip
RCON_PORT=your_server_port
RCON_PASSWORD=your_rcon_password
UPDATE_INTERVAL=10
```

4. **Run the bot:**

```bash
python bot.py
```

## Notes

* Make sure RCON is properly configured in your `servertest.ini`:

  ```ini
  RCONPort=your_server_port
  RCONPassword=your_rcon_password
  RCONEnabled=true
  ```
* The bot's status will automatically update every `UPDATE_INTERVAL` seconds to reflect the current player count.

Made with ☕ for the Project Zomboid community.
