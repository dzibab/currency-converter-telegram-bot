from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from api import TELEGRAM_BOT_TOKEN
from convert_currency import convert_currency


async def convert_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        args = text.split()
        if len(args) != 3:
            raise ValueError("Please provide input in the format: '<amount> <from_currency> <to_currency>'")
        amount, from_currency, to_currency = args
        amount = float(amount)
        result = convert_currency(amount, from_currency, to_currency)
        await update.message.reply_text(f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I can convert currencies.\n"
        "Use me like this:\n"
        "`100 usd eur`",
        parse_mode="Markdown"
    )


def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_message))
    app.run_polling()


if __name__ == "__main__":
    run_bot()
