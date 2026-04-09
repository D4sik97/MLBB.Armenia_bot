import string
import random
import time
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# TOKEN = os.getenv("TELEGRAM_TOKEN")
TOKEN = "8793230627:AAFAc987PxepN-5ELULae-TQpNL67_xgH3o"

namewewew = "Aram"

last_reply_time = {}
# Приветствие новых участников
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"Բարի գալուստ {user.first_name} 🎮🔥\n"
            "Շնորհավորում ենք ձեզ մեր community-ին անդամ դառնալու առթիվ 🤝\n"
            "Մաղթում ենք հաճելի խաղեր, ակտիվ մասնակցություն և լավ թիմային հաղթանակներ 🏆"
        )

# Общий автоответ на ключевые слова
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_id = update.message.from_user.id
    now = time.time()

    # анти-спам: 20 секунд
    if user_id in last_reply_time and now - last_reply_time[user_id] < 10:
        return

    text = update.message.text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    hello_keywords = ["barior", "barev", "baylus", "priv", "բարև"]
    how_keywords = ["voncek","vonc","inchpes","vonceq", "lavek","laveq"]
    how2_keywords = ["inch ka","inch ka chka","inch ek anum"]
    manvelAlmaz_keywords = ["almaz","almazner"]
    Armen_keywords = ["armen","Armen","armeni","armenia"]
    Zzvcrir_keywords = ["zzvcrik","zzva","zzvcrir","zzveli","zzvum em"]
    Gor_keywords = ["gor","gorik","goro"]
    Ed_keywords = ["ed","edik","edikyan"]
    Ero_keywords = ["ero","erik",]
    Jin_keywords = ["jin","jino","jinoyan"]
    Lyov_keywords = ["lyov","levon","lev",]
    Raf_keywords = ["raf","rafo","rafik","rafayel"]
    Vova_keywords = ["vova","vovik","vov","vovikyan"]
    Manvel_keywords = ["manvel","manvelik","manvelyan"]
    Daniel_keywords = ["daniel","danik","dani","dan","danielyan"]
    Lerno_keywords = ["lerno","lernik","lerni","lern","lernelyan"]
    Hayko_keywords = ["hayko","hayk","haykik"]
    Aram_keywords = ["aram","aramik","aramyan"]
    Jox_keywords = ["jox","joxovurd","joxs"]
    Amali_keywords = ["amali","amalik","amaliyan","amalya"]
    Vahagn_keywords = ["vahagn","vahag","vahe"]
    Klaus_keywords = ["klaus","klausi","klausan"]
    Gisher_keywords = ["gisher","gisheri","gisheryan"]
    Dav_keywords = ["dav","davi","david"]
    Kost_keywords = ["kost","kostik","kostyan"]
    Frunz_keywords = ["frunz","frunzik","frunzyan"]
    Harut_keywords = ["harut","harutikkkk","harutyunyan"]








    # используем elif, чтобы бот ответил только один раз
    if any(word in text for word in hello_keywords):
        await update.message.reply_text("Բարի Լույս😎")
        last_reply_time[user_id] = now

    elif any(word in text for word in how_keywords):
        await update.message.reply_text("Լավ ապրես, դուք ոնց եք?☺️")
        last_reply_time[user_id] = now

    elif any(word in text for word in how2_keywords):
        await update.message.reply_text("Բան չէ դու ասա 😊")
        last_reply_time[user_id] = now

    elif any(word in text for word in manvelAlmaz_keywords):
        await update.message.reply_text("ես լսեցի Ալմա՞զ Կանչում եմ Մանվելին😅")
        last_reply_time[user_id] = now

    elif any(word in text for word in Armen_keywords):
        videos = [
            "Armen.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Zzvcrir_keywords):
        videos = [
            "Zzvcrir.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Gor_keywords):
        videos = [
            "Gor.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Ed_keywords):
        videos = [
            "Ed.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Ero_keywords):
        videos = [
            "Ero.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Jin_keywords):
        videos = [
            "Jin1.MP4",
            "Djin.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Lyov_keywords):
        videos = [
            "Lyov.MP4",
            
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Raf_keywords):
        videos = [
            "Raf1.MP4",
            "Raf2.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Vova_keywords):
        videos = [
            "Vova.mp4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Manvel_keywords):
        videos = [
            "Manvel.MP4",
            "Manvel2.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Daniel_keywords):
        videos = [
            "Dan1.MP4",
            "Dan2.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Lerno_keywords):
        videos = [
            "Lerno.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Hayko_keywords):
        videos = [
            "Hayko.mp4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Jox_keywords):
        videos = [
            "jox.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Aram_keywords):
        videos = [
            "Aram.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Amali_keywords):
        videos = [
            "Amali.MP4",
            "Amali2.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)
            

    elif any(word in text for word in Vahagn_keywords):
        videos = [
            "Vahag.MP4",
            "Vahag2.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Klaus_keywords):
        videos = [
            "Klaus.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Gisher_keywords):
        videos = [
            "Gisher.MP4",
            "Gisher1.MP4",
            "Gisher2.MP4",
            "Gisher3.MP4",
            "Gisher4.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now   

    elif any(word in text for word in Dav_keywords):
        videos = [
            "Dav.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now

    elif any(word in text for word in Kost_keywords):
        videos = [
            "Kost.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now


    elif any(word in text for word in Frunz_keywords):
        videos = [
            "Frunz.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now


    elif any(word in text for word in Harut_keywords):
        videos = [
            "Harut.MP4",
        ]

        video_path = random.choice(videos)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video)

        last_reply_time[user_id] = now           

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Բոտը աշխատում է...")
app.run_polling()