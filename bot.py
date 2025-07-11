from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from g4f.client import Client
from g4f.Provider import FreeGpt  # Provider gratis yang tidak pakai cookies

BOT_TOKEN = "7648869904:AAE38kPxaH32oNZTxvpHtCR1m1CyUTEWddw"

client = Client(provider=FreeGpt, enable_browser=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim pesan apa saja dan aku akan membalas dengan ChatGPT (versi gratis) 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # gpt-4o sering error di provider gratis
            messages=[{"role": "user", "content": update.message.text}],
        )
        await update.message.reply_text(response.choices[0].message.content.strip())
    except Exception as e:
        await update.message.reply_text(f"⚠️ Terjadi error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
