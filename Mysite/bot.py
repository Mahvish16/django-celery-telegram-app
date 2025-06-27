import os
import django
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mysite.settings')  
django.setup()

load_dotenv()

from Demo.models import Telegrambot

@sync_to_async
def save_user_to_db(user):
    Telegrambot.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username 
            
        }
    )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await save_user_to_db(user)
    await update.message.reply_text(
        f"Hi { user.username}, welcome to the bot!"
    )

def main ():
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
