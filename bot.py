from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
import threading
import os

TOKEN = os.getenv"8987496794:AAE0QhsB4D_HtF6ukpimZvZzn_afN3aWpeY"

# سيرفر Web لـ Render
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running ✅"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 🌹\n"
        "أرسل:\n"
        "المنتجات\n"
        "الأسعار\n"
        "طريقة الطلب"
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "المنتجات" in text:
        await update.message.reply_text(
            "لدينا: قهوة ☕ - شاي 🍵 - عسل 🍯"
        )

    elif "الأسعار" in text:
        await update.message.reply_text(
            "أرسل اسم المنتج لمعرفة السعر."
        )

    elif "طريقة الطلب" in text:
        await update.message.reply_text(
            "أرسل اسم المنتج + اسمك + رقم الهاتف."
        )

    else:
        await update.message.reply_text(
            "لم أفهم طلبك."
        )


def main():
    threading.Thread(target=run_web).start()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
