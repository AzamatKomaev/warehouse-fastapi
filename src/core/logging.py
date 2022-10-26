import logging


_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
formatter = logging.Formatter(_log_format)


logger = logging.getLogger('custom_recipes')
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('uvicorn.log')

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
