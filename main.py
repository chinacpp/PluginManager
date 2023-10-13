from PluginManager import PluginManger

if __name__ == '__main__':
    plugins = PluginManger()
    plugins.load_plugins()
    print('*' * 50)
    plugins.process()
