import logging
import os
from datetime import datetime
import exception
import sys

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs will be stored in a folder named 'log' with the above file name convetion

logs_path = os.path.join(os.getcwd(),"log",LOG_FILE)
os.makedirs(logs_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":

    try:
        a = 1/0
    
    except Exception as e:
        logging.info('Divide by zero')
        raise exception.CustomException(e,sys)

    logging.info("Logging begins here")