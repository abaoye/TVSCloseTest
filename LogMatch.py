import queue
import threading
import StateMachine

class LogMatch(threading.Thread):
    def __init__(self, threadName):
        super(LogMatch, self).__init__(name = threadName)
        self.log_que = queue.Queue()
        self.name = threadName
        self.tvs_handle = (0, 0)
        self.tid = 0
        self.state_machine = StateMachine()
        self.stop_flag = True

    def start(self):
        self.stop_flag = False
        self.state_machine.add_state("LOG_INVALID", st_invalid)
        self.state_machine.add_state("LOG_SUCCESS", st_success)
        self.state_machine.add_state("LOG_FAILED", st_failed)
        self.state_machine.add_state("LOG_OVER", None, end_state=1)
        super(LogMatch, self).start()
        
    def run(self):
        self.state_machine.set_start("LOG_INVALID")
        self.state_machine.run()
             

    def stop(self):
        self.stop_flag = True

    def st_invalid(self, cargo):
        item = self.que.get()
        return (newState, item)

    def st_success(self, cargo):
        print "Success"
        return ("LOG_OVER", cargo)
        

    def st_failed(self, cargo):
        print "Failed"
        return ("LOG_OVER", cargo)
        