import RouterProxy

class TVSConnection(object):
    def __init__(self):
        self.routerProxy = RouterProxy.get_instance()


    def call(self,cmd):
        self.routerRroxy.call(cmd)
