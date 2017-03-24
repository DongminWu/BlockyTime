class MyConfig:
    __config = {
        "debug_message": True,
        "version": "1.0",
        "database_path": "database/data.sqlite",
        "host": "0.0.0.0",
        "port": 5000
    }

    def __init__(self):
        pass

    def getConfig(self, config_name):
        ret = None
        try:
            ret = self.__config[config_name]
        except Exception, e:
            print("The key did not exist in Config")
        finally:
            if (ret != None):
                return ret
