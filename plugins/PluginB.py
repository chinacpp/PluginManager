from Plugin import BasePlugin


class PluginB(BasePlugin):

    def __init__(self):
        super().__init__()
        print('PluginB 初始化')

    def enter(self):
        print('PluginB enter')

    def exit(self):
        print('PluginB exit')