import logging
import time
class LogGen:

    @staticmethod
    def loggen():
        #dateTimeStamp = time.strftime('%Y_%m_%d_%H_%M')
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s : %(name)s : %(levelname)s : %(message)s' , datefmt='%d-%m-%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger