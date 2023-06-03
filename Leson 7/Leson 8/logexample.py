from logging import debug, info, warning, error, critical


class ILog:
    def __init__(self, message=""):
        self.Message = message

    def __str__(self):
        if self.Message == "":
            raise Exception("log message is empty")
        return self.Message

    def LogData(self):
        debug(self.Message)
        info(self.Message)
        warning(self.Message)
        error(self.Message)
        critical(self.Message)
