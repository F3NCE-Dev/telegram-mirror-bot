# Mirror-Bot

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

---

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
