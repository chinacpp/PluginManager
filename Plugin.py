import abc

class BasePlugin(metaclass=abc.ABCMeta):

    def __init__(self):
        print('BasePlugin 初始化')

    @abc.abstractmethod
    def enter(self):
        pass

    @abc.abstractmethod
    def do(self):
        pass

    @abc.abstractmethod
    def exit(self):
        pass