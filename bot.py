from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import g4f

BOT_TOKEN = "7648869904:AAE38kPxaH32oNZTxvpHtCR1m1CyUTEWddw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim pesan apa saja dan aku akan membalas dengan ChatGPT (gratis) 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",  # pakai model gratis dan stabil
            provider=g4f.Provider.FreeChat,  # provider stabil tanpa perlu cookie
            messages=[{"role": "user", "content": update.message.text}],
        )
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"⚠️ Terjadi error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
