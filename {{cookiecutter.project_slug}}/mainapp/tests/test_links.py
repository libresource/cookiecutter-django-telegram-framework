from telegram_framework.test import SimpleTestCase


class TestCommands(SimpleTestCase):


    def test_introduction(self):
        """
        Test /start: success
        """
        chat = self.assertCommandWasHandled('/start', self.chat)
        self.assertChatLastMessageTextEqual(chat, '<b>Demo</b> 👋')
