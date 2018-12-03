import logging


# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)

        handler = logging.FileHandler("log.txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)

        self.logger.addHandler(handler)
        self.logger.addHandler(console)
        self.submodule = None

    def debug(self, msg, *args, **kwargs):
        if self.submodule is None:
            self.logger.debug(msg, *args, **kwargs)
        else:
            msg = self.submodule + ": " + str(msg)
            self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        if self.submodule is None:
            self.logger.info(msg, *args, **kwargs)
        else:
            msg = self.submodule + ": " + str(msg)
            self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        if self.submodule is None:
            self.logger.warning(msg, *args, **kwargs)
        else:
            msg = self.submodule + ": " + str(msg)
            self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if self.submodule is None:
            self.logger.error(msg, *args, **kwargs)
        else:
            msg = self.submodule + ": " + str(msg)
            self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        if self.submodule is None:
            self.logger.critical(msg, *args, **kwargs)
        else:
            msg = self.submodule + ": " + str(msg)
            self.logger.critical(msg, *args, **kwargs)

    def __call__(self, name):
        self.submodule = name
        return self


logger = Logger()

