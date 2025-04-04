from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from api import TELEGRAM_BOT_TOKEN
from convert_currency import convert_currency


async def convert_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount, from_currency, to_currency = context.args
        amount = float(amount)
        result = convert_currency(amount, from_currency, to_currency)
        await update.message.reply_text(f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I can convert currencies.\n"
        "Use me like this:\n"
        "`/convert 100 usd eur`",
        parse_mode="Markdown"
    )


def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("convert", convert_command))
    app.run_polling()


if __name__ == "__main__":
    run_bot()
