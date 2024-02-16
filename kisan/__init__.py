import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.flood_420 import FloodWait
from .config import Config
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if Config.STRING_SESSION:
    app = Client(api_id=Config.API_ID, api_hash=Config.API_HASH, session_name=Config.STRING_SESSION)

if Config.BOT_TOKEN:
    bot = Client(":memory:", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

async def delete_sticker(message):
    await asyncio.sleep(300)  # Wait for 5 minutes
    await message.delete()

async def delete_video(message):
    if message.video:
        await message.delete()

if Config.STRING_SESSION:
    @app.on_message(filters.sticker)
    async def handle_sticker(bot, msg):
        asyncio.create_task(delete_sticker(msg))

    @app.on_message(filters.video)
    async def handle_video(bot, msg):
        asyncio.create_task(delete_video(msg))

    @app.on_message(filters.edited)
    async def handle_edited_message(bot, msg):
        await msg.delete()

if Config.BOT_TOKEN:
    @bot.on_message(filters.sticker)
    async def handle_sticker(bot, msg):
        asyncio.create_task(delete_sticker(msg))

    @bot.on_message(filters.video)
    async def handle_video(bot, msg):
        asyncio.create_task(delete_video(msg))

    @bot.on_message(filters.edited)
    async def handle_edited_message(bot, msg):
        await msg.delete()

if Config.BOT_TOKEN:
    @bot.on_message(filters.command(["start"]))
    async def start_command(bot, message):
        await message.reply("This bot works only in groups and automatically deletes stickers after 5 minutes. "
                            "It also deletes edited messages and video files.")

if __name__ == "__main__":
    app.run()
    bot.run()
