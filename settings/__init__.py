__author__ = 'can'

import os


if os.environ.get('SCRAPER_PROD') is not None:
    import settings.prod as settings
else:
    import settings.dev as settings


import logging
import logging.handlers

# Logger Configuration
LOG_FILEPATH = settings.LOGGING_DIR + "/scraper.log"
logging.basicConfig(level=settings.LOG_LEVEL, format="%(asctime)s : %(levelname)s : %(message)s", filename=LOG_FILEPATH)
logger = logging.getLogger("Scraper")


# logger.addHandler(
#     logging.handlers.TimedRotatingFileHandler(LOG_FILEPATH,
#                                        when="midnight",
#                                        interval=1,
#                                        backupCount=5)
# )
