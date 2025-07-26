from datetime import datetime

class LogMessage:

    def __init__(self,message,logLevel):
        self.message = message
        self.logLevel = logLevel
        self.timestamp = datetime.now()


    def getMessage(self):
        return self.message
    
    def getLogLevel(self):
        return self.logLevel
    
    def getTimestamp(self):
        return self.timestamp
    
    def __str__(self):
        return f"{self.timestamp} - {self.logLevel}: {self.message}"