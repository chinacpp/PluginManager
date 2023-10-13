import importlib
import glob
import os
import inspect
from Plugin import BasePlugin


class PluginManger:

    def __init__(self):
        self.plugins = []

    def load_plugin(self, module_name):
        # 导入模块
        module = importlib.import_module(module_name)
        # 获得所有满足条件类对象
        def predicate(module):
            if not isinstance(module, type):
                return False
            if not issubclass(module, BasePlugin) or module is BasePlugin:
                return False
            return True
        classes = inspect.getmembers(module, predicate=predicate)
        return classes

    def load_plugins(self):

        # 1. 加载模块中类对象
        module_names = glob.glob('plugins/*.py')
        my_classes = []
        for mudule_name in module_names:
            module_name, extension = os.path.splitext(mudule_name)
            module_name = module_name.replace(os.path.sep, '.')
            classes = self.load_plugin(module_name)
            my_classes.extend(classes)

        # 2. 实例化插件对象
        for _, my_class in my_classes:
            try:
                print('-----插件', my_class.__name__, '初始化-----')
                object = my_class()
                self.plugins.append(object)
            except Exception as error:
                print('Error: 插件初始化失败，原因: ', error)

    def process(self):
        for plugin in self.plugins:
            print('-----插件', plugin.__class__.__name__, '执行-----')
            plugin.enter()
            plugin.do()
            plugin.exit()
