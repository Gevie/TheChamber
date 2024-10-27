import asyncio
import logging
from src.bot import BotRunner
from server import ServerRunner

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Application:
    def __init__(self):
        self.bot_runner = BotRunner()
        self.server_runner = ServerRunner()
        logger.debug('Application initialized.')

    def run(self):
        logger.debug('Starting server...')
        self.server_runner.start()
        logger.info('Server started.')

        try:
            logger.debug('Starting bot...')
            asyncio.run(self.bot_runner.run())
        except Exception as e:
            logger.error(f'Error running bot: {e}')
        finally:
            logger.debug('Stopping server...')
            self.server_runner.stop()
            logger.info('Server stopped.')


if __name__ == '__main__':
    logger.info('Starting Application...')
    app = Application()
    app.run()