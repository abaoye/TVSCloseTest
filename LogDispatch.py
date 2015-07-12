import threading
import queue
import LogMatch
import json

class LogDispatch(threading.Thread):
    __instance = None
  
    
    def __init__(self, threadName):
        super(RouterProxy, self).__init__(name = threadName)
        self.que = queue.Queue()
        self.stop_flag = True
        self.log_matches = {}
        fp = open("logTemp.json")
        self.log_temp = json.dumps(fp.read())

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls.__instance = RouterProxy()
        return cls.__instance

    def run(self):
        while(!self.stop_flag):
            item = self.que.get()
            if item["tag"] == "TVSAPI":
                mt = get_log_match(item)
                if mt:
                    self.log_match.update(mt)
                
            else if item["tag"] == "SIGNAL":
                //
            else if item["tag"] == "LOG"
                self.send_log_to_match(item["data"])
                
                
    def stop(self):
        self.stop_flag = True

    def send(self, item):
        self.que.put(item)

    def get_log_match(self, item):
        # get main thread id
        if not self.log_temp[item["func"]]:
            return
        log_match = LogMatch()
        log_match.load_temp()
        log_match.start()
        mt = {item["TVS_HANDLE"], log_match}
        return mt

    def send_log_to_match(self, log):
        tid = get_log_tid(log)
        self.log_match[log[]]

    def get_log_tid(self, log):
        index = log.find("TID")

        return log[2:4]
