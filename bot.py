from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8987496794:AAE0QhsB4D_HtF6ukpimZvZzn_afN3aWpeY"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 🌹\n"
        "أرسل كلمة:\n"
        "المنتجات\n"
        "الأسعار\n"
        "طريقة الطلب"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "المنتجات" in text:
        await update.message.reply_text("لدينا: قهوة - شاي - عسل - مكملات غذائية")

    elif "الأسعار" in text:
        await update.message.reply_text("أرسل اسم المنتج لمعرفة سعره.")

    elif "طريقة الطلب" in text:
        await update.message.reply_text("أرسل اسم المنتج واسمك ورقم هاتفك لإتمام الطلب.")

    else:
        await update.message.reply_text("عذراً، لم أفهم طلبك.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
