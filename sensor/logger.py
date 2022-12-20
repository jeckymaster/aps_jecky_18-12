import logging
import os
from datetime import datetime 

#Log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#Log Directry
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#Creat folder if not available
os.makedirs(LOG_FILE_DIR, exits_ok = True)

# log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asktime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

