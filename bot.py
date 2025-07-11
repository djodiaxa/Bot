from revChatGPT.V1 import Chatbot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# Ambil dari environment variable
config = {
    "email": os.getenv("GPT_EMAIL"),
    "password": os.getenv("GPT_PASSWORD")
}

chatbot = Chatbot(config)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim pesan apa saja dan aku akan jawab pakai ChatGPT gratis 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = ""
        for data in chatbot.ask(update.message.text):
            response += data["message"]
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"❌ Terjadi error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
