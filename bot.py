import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
IMAGE_URL = "https://ibb.co/B5QXY1B8/photo-2026-05-15-22-03-17.jpg"

WELCOME_MESSAGE = (
    "Qoutex Compounding series group click this link 🔗 👇\n\n"
    "https://t.me/+YsiZbHY4b4MwMGY9\n"
    "https://t.me/+YsiZbHY4b4MwMGY9\n\n"
    "🔥 Just 7 Days Challenge! 🔥\n"
    "Turn $30 → $1000 💸\n"
    "Limited slots — Join Fast & Start Earning Now! 🚀"
)

async def handle_join_request(update, context):
    user = update.chat_join_request.from_user
    chat_id = user.id
    keyboard = [[InlineKeyboardButton("✅ Join Group Now", url="https://t.me/+38IXH_QUK6EyMWY1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=IMAGE_URL,
            caption=WELCOME_MESSAGE,
            reply_markup=reply_markup
        )
        logger.info(f"Welcome sent to {user.first_name}")
        # await update.chat_join_request.approve()
    except Exception as e:
        logger.error(f"Error: {e}")

async def post_init(application):
    await application.bot.delete_webhook(drop_pending_updates=True)

def main():
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    logger.info("Bot started 24/7!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
