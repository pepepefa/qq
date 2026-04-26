from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7973091125:AAFcTBw6M4P6lMU_vfU52IZA3BP99q0OGtw"

async def dice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message and message.dice:
        dice = message.dice

        # Перевірка що це слот 🎰
        if dice.emoji == "🎰":
            
            # 777 = 64
            if dice.value == 64:
                user = message.from_user

                name = user.first_name
                username = f"@{user.username}" if user.username else name

                await message.reply_text(
                    f"🎉 {username} выбил 777!!!"
                )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.Dice.ALL, dice_handler))

print("Бот запущений...")
app.run_polling()