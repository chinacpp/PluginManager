from Plugin import BasePlugin


class PluginA(BasePlugin):

    def __init__(self):
        super().__init__()
        print('PluginA 初始化')

    def enter(self):
        print('PluginA enter')

    def do(self):
        print('PluginA do')

    def exit(self):
        print('PluginA exit')