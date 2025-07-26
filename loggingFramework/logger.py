
from util import LogAppender
from logMessage import LogMessage

class Logger:

    __instance = None
    __isInitialized = False

    def __new__(cls,*args,**kawargs):
        if cls.__instance is None:
            cls.__instance = super(Logger,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self,appenders:list[LogAppender]=None):
        if self.__isInitialized:
            print('not reinitializing the object again')
            return
        self.logMessage = None
        self.appenders = appenders


    def log(self,logMessage:LogMessage):
        for appender in self.appenders:
            appender.append(logMessage)
        print(f" printing log Message on logger {logMessage.getLogLevel()} : {logMessage.getMessage()} : {logMessage.getTimestamp()}")

    def addAppender(self, appender:LogAppender):
        self.appenders.append(appender)

    def removeAppender(self, appender:LogAppender):
        self.appenders.remove(appender)




        
    

        

