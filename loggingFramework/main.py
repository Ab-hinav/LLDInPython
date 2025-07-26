
from logger import Logger
from logMessage import LogMessage
from util import LOGLEVEL
from util import ConsoleLogAppender,DBLogAppender


if __name__ == '__main__':
    print("Hello World")

    logMesg = LogMessage("this is a log message",LOGLEVEL.DEBUG)
    consoleAppend = ConsoleLogAppender()
    dbAppend = DBLogAppender()

    logger = Logger([consoleAppend,dbAppend])
    
    logger.log(logMesg)