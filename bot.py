import string
import random
import time
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")
# TOKEN = "8793230627:AAFAc987PxepN-5ELULae-TQpNL67_xgH3o"


last_reply_time = {}
# Приветствие новых участников
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Բարի գալուստ {user.first_name} 🎮🔥\n"
            "Շնորհավորում ենք ձեզ մեր community-ին անդամ դառնալու առթիվ 🤝\n"
            "Մաղթում ենք հաճելի խաղեր, ակտիվ մասնակցություն և լավ թիմային հաղթանակներ 🏆"
        )



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))


print("Բոտը աշխատում է...")
app.run_polling()