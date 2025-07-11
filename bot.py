from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from revChatGPT.V1 import Chatbot

TELEGRAM_TOKEN = "7648869904:AAE38kPxaH32oNZTxvpHtCR1m1CyUTEWddw"

chatbot = Chatbot({
    "email": "aniesmas591@gmail.com",
    "password": "Lala011199*#"
})

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    try:
        response = ""
        for data in chatbot.ask(user_message):
            response += data["message"]
        await context.bot.send_message(chat_id=chat_id, text=response)
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
