from telegram import Bot
import test.config as config

from actions import Callback

from core import BotHive

# Actions

hello = Callback()


@hello
async def _hello(session):
    session.bot.send_message(chat_id=session.chat_id,
                             text="Meow")


if __name__ == '__main__':
    bot = Bot(config.token)
    h = BotHive(bot)
    h.start()
    h.idle()
