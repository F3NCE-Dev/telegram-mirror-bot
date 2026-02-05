# Telegram-mirror-bot

This Telegram bot allows you to create "branches" of channels and send messages to all selected channels at once.  

**Idea:** Write a message once and forward it to multiple channels simultaneously.

---

## Features

- Create and remove branches
- Rename branches
- Enable or disable branches
- Support for all message types:
  - Text
  - Photo
  - Video
  - Audio
  - Document
  - Sticker
  - Voice message
- Can add extra text to message
- View your branches and extra messages

## Local installation

### Step 1: Clone the repository

```bash
git clone https://github.com/F3NCE-Dev/telegram-mirror-bot
cd telegram-mirror-bot
```

### Step 2: Install requirements.txt

Create a venv

```bash
python -m venv venv

source venv/bin/activate # for Linux/Mac
# or
venv/Scripts/activate # for windows
```

Install the requirements

```bash
pip install -r requirements.txt
```

### Step 3: Create a file named *.env*

```bash
echo "" > .env
```

Add  required variables

Example:

```bash
BOT_TOKEN="your bot token"
DATABASE_URL="your database url"
```

### Step 4: Run the bot

```bash
python bot.py
```

## Commands

- `/id` — show your chat and user ID  
- `/create` — create a channel branch  
- `/remove` — remove your channel branch  
- `/rename` — rename your channel branch  
- `/list` — view your branches
- `/addition` — add an extra text to messages  
- `/remove_addition` — remove your extra message  
- `/viewad` — view your extra message  
- `/switch` — change your branch status
- `/cancel` — cancel the current action

## Tech Stack

- **aiogram**
- **SQLAlchemy**
- **pydantic-settings**
