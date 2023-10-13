from Plugin import BasePlugin


class PluginC(BasePlugin):

    def __init__(self):
        super().__init__()
        print('PluginC 初始化')

    def enter(self):
        print('PluginC enter')

    def do(self):
        print('PluginC do')

    def exit(self):
        print('PluginC exit')