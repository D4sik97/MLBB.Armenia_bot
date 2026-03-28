import string
import time
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

last_reply_time = {}
# Приветствие новых участников
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Բարու գալուստ {user.first_name} 🎮🔥\n"
            "Շնորհավորում ենք քեզ մեր community-ին անդամ դառնալու առթիվ 🤝\n"
            "Մաղթում ենք հաճելի խաղեր, ակտիվ մասնակցություն և լավ թիմային հաղթանակներ 🏆"
        )

# Общий автоответ на ключевые слова
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_id = update.message.from_user.id
    now = time.time()

    # анти-спам: 10 секунд
    if user_id in last_reply_time and now - last_reply_time[user_id] < 10:
        return

    text = update.message.text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    hello_keywords = ["barior", "barev", "baylus", "priv", "բարև"]
    how_keywords = ["voncek","vonc","inchpes","vonceq", "lavek","laveq"]
    how2_keywords = ["inch ka","inch ka chka","inch ek anum"]

    # используем elif, чтобы бот ответил только один раз
    if any(word in text for word in hello_keywords):
        await update.message.reply_text("Բարի Լույս😎")
        last_reply_time[user_id] = now

    elif any(word in text for word in how_keywords):
        await update.message.reply_text("Լավ ապրես, դու ոնց ես?☺️")
        last_reply_time[user_id] = now

    elif any(word in text for word in how2_keywords):
        await update.message.reply_text("Բան չէ դու ասա 😎")
        last_reply_time[user_id] = now

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Բոտը աշխատում է...")
app.run_polling()