import asyncio
from src.bot import BotRunner
from server import ServerRunner


class Application:
    def __init__(self):
        self.bot_runner = BotRunner()
        self.server_runner = ServerRunner()

    def run(self):
        self.server_runner.start()

        try:
            asyncio.run(self.bot_runner.run())
        finally:
            self.server_runner.stop()


if __name__ == '__main__':
    app = Application()
    app.run()
