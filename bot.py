
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from g4f.client import Client
from g4f.Provider import GeekGpt  # Gratis, cepat, stabil

BOT_TOKEN = os.getenv("BOT_TOKEN")
client = Client(provider=GeekGpt)

SYSTEM_PROMPT = (
    "Kamu adalah chatbot dengan gaya sarkas, nyolot, tapi lucu. "
    "Jawabanmu santai kayak teman tongkrongan, suka roasting, tapi tetap informatif."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo! Bot udah nyala, tinggal nanya. Jangan bego aja 😏")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )
        await update.message.reply_text(response.choices[0].message.content.strip())
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
