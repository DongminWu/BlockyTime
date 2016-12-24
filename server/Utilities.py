from MyConfig import MyConfig

def debug_msg(msg):
    a = MyConfig()
    if (a.getConfig("debug_message") == True):
        print "[debug]"+str(msg)
    
