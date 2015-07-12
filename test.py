
class State(object):
    def ss(self, ptr):
        ptr()

    def add(self):
        print "hello"

if __name__ == "__main__":
    s = State()
    s.ss(s.add)
