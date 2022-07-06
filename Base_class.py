import inspect
import logging

class Base_class:
    def getLogger(self):
        loggername= inspect.stack()[1][3]
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
