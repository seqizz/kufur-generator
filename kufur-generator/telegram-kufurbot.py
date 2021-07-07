#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import logging
from uuid import uuid4
from os import getenv
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    InlineQueryHandler,
)
from telegram import InlineQueryResultArticle, InputTextMessageContent
from kufur import kufur

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(bot, update):
    bot.message.reply_text(
        "Hoşgeldin. Bu bot tüm mesajlarına küfürle karşılık verir."
    )


def echo(bot, update):
    bot.message.reply_text(kufur())


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        query = str(uuid4())
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query,
            title='Bana kufret',
            input_message_content=InputTextMessageContent(
                kufur(),
                parse_mode='Markdown'
            )
        )
    )
    update.inline_query.answer(results, cache_time=2)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(
        getenv('TELEGRAM_TOKEN'),
        use_context=True
    )

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    #  inline_caps_handler = InlineQueryHandler(inline_caps)
    dp.add_handler(InlineQueryHandler(inline_caps))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
