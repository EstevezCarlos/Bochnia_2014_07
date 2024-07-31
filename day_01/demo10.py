import logging
from demo11 import my_function
logging.basicConfig(level=logging.CRITICAL)

logger = logging.getLogger('xxx')
logger.setLevel(logging.DEBUG)

x  = 6567

logger.error(x)
logger.warning(x)
logger.info(x)
logger.debug(x)


my_function()
y = x/3
print(y)