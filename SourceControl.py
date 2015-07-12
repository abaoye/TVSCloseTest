import TVSConnection

class SourceControl(TVSConnection):
    def __init__(self):
        super(SourceControl, self).__init__()

    def SetSource(self, sourceType):
        self.call(sourceTuype)
