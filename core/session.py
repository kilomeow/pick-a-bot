from base import TelegramSession


class ChatSession(TelegramSession):
    def __init__(self, worker, bot, chat_id):
        super().__init__(worker, bot)
        self.chat_id = chat_id
