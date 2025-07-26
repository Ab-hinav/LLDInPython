from enum import Enum

from abc import ABC, abstractmethod


class LOGLEVEL(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


class LogAppender(ABC):

    @abstractmethod
    def append(self, logMessage):
        pass



class ConsoleLogAppender(LogAppender):

    def append(self, logMessage):
        print(f" printing log Message on console {logMessage.getLogLevel()} : {logMessage.getMessage()} : {logMessage.getTimestamp()}")


class DBLogAppender(LogAppender):

    def append(self, logMessage):
        print(f" printing log Message on DB {logMessage.getLogLevel()} : {logMessage.getMessage()} : {logMessage.getTimestamp()}")