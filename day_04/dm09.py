from decouple import config
import logging

logging.basicConfig(level=int(config('LOG_LEVEL')))
USER = config('USER')
PASSWORD = config('PASSWORD')
SERVER = config('SERVER')

logging.debug(USER)
logging.info(PASSWORD)
logging.warning(SERVER)
