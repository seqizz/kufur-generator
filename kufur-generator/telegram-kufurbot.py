#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import logging
from uuid import uuid4
from os import getenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
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


async def start(update, context):
    await context.bot.send_message(chat_id=update.message.chat_id, text=(
        "Hoşgeldin. Bu bot tüm mesajlarına küfürle karşılık verir."
    ))


async def echo(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=kufur())


async def inline_caps(update, context):
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
    await context.bot.answer_inline_query(update.inline_query.id, results, cache_time=0)


def main():
    dp = Application.builder().token(getenv('TELEGRAM_TOKEN')).build()  # type: ignore

    # on different commands - answer in Telegram
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    dp.add_handler(inline_caps_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    dp.add_handler(echo_handler)

    # Start the Bot
    dp.run_polling()


if __name__ == '__main__':
    main()
