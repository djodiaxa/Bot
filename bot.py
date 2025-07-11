import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from revChatGPT.V1 import Chatbot

# Inisialisasi chatbot dengan email & password dari environment variable
chatbot = Chatbot(config={
    "email": os.getenv("GPT_EMAIL"),
    "password": os.getenv("GPT_PASSWORD")
})

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim pesan apa saja dan aku akan membalas dengan ChatGPT (versi gratis) 🤖")

# Menangani pesan teks biasa
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text
        response = ""
        for data in chatbot.ask(user_input):
            response += data["message"]

        await update.message.reply_text(response.strip())

    except Exception as e:
        await update.message.reply_text(f"⚠️ Terjadi error: {e}")

# Menjalankan bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
