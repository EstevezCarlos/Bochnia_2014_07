import logging

logging.basicConfig(level=20)

logger_1 = logging.getLogger('logger for my_function_1')
logger_2 = logging.getLogger('logger for my_function_2')
logger_1.setLevel(logging.DEBUG)
logger_2.setLevel(logging.DEBUG)

logging.info(' You are running my awesome program.')

def my_fuction_1():
    x = 3
    logger_1.info(x)

my_fuction_1()

    
def my_fuction_2():
    x = 3
    logger_2.debug(x)

my_fuction_2()