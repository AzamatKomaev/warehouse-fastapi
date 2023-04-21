import pathlib
import logging


current_dir = pathlib.Path(__file__).parent.parent.parent.resolve()

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
formatter = logging.Formatter(_log_format)


logger = logging.getLogger('custom_recipes')
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(current_dir / 'uvicorn.log')

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

c_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logger.addHandler(c_handler)
logger.addHandler(f_handler)
