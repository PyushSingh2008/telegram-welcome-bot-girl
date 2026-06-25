import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user
    try:
        await context.bot.approve_chat_join_request(
            chat_id=CHANNEL_ID,
            user_id=user.id
        )
        keyboard = [[InlineKeyboardButton("📢 JOIN CHANNEL", url="https://t.me/Qx_With_Rohit_Bot")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        caption = (
            f"🔥📈 Hey {user.first_name}!\n\n"
            "Want *10 FREE NON MTG BUG Quotex Signals?*\n\n"
            "👇 Join our VIP channel now!\n\n"
            "✅ High Accuracy Signals\n"
            "✅ Daily Updates\n"
            "✅ 100% Free to Join"
        )
        with open("welcome.png", "rb") as photo:
            await context.bot.send_photo(
                chat_id=user.id,
                photo=photo,
                caption=caption,
                parse_mode="Markdown",
                reply_markup=reply_markup
            )
        logger.info(f"Welcomed: {user.first_name} ({user.id})")
    except Exception as e:
        logger.error(f"Error: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    logger.info("Bot started...")
    app.run_polling()

if name == "main":
    main()
