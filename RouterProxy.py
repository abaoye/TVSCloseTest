import threading
import socket
import LogDispatch

class RouterProxy(threading.Thread):
    __instance = None
    BUFSIZ = 1024
    
    def __init__(self, threadName):
        super(RouterProxy, self).__init__(name = threadName)
        self.port = 8001
        self.ip = ""
        self.stop_flag = True
        self.client=socket(AF_INET, SOCK_STREAM)
        self.rtn_value = ""
        self.logDispatch = LogDispatch.get_instance()
        self.cond = threading.Condition()
        

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls.__instance = RouterProxy()
        return cls.__instance

    def set_host(self, host):
        self.host = host

    def start(self):
        self.stop_flag = False
        self.client.connect((self.host, self.port))
        super(RouterProxy,self).start()
        
    def run(self):
        while(!self.stop_flag):
            data = self.client.recv(self.BUFSIZ)
            if data["tag"] == "RTN":
                self.cond.acquire()
                rtn_value = data["data"]
                self.cond.notify()
                self.cond.release()
                
            else if data["tag"] == "SIGNAL":
                //
            else if data["tag"] == "LOG":
                self.logDispatch.send(data)

    def stop(self):
        self.stop_flag = True

    def call(self,data):
        self.logDispatch.send(data)
        self.cond.acquire()
        self.client.send(data)
        self.cond.wait()
        self.cond.release()
        return self.rtn_value
        


        
        
