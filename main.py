class Array():
    def __init__(self, nElems):
        self.a = []
        self.nElems = nElems

    def GetSetDelArrayFunc(self, size):
        self.a = [size]
        self.nElems = 0

    def getNumEle(self):
        return self.nElems

    
