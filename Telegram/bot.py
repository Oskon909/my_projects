import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


# https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/fajlami-media-url-adresami/
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('test', 'rb'))


if __name__ == '__main__':
    application = ApplicationBuilder().token('5315599976:AAFQo11VxD-jRAF9tVC6oNEqsfDowvGq1QQ').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
