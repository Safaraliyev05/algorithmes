class OrdArray():
    def __init__(self):
        self.a = []
        self.nElems = 0
        self.ele = 0
        self.size = 0

    def size(self):
        return self.nElems

    def getElementFromPos(self, index):
        return self.a[index]

    def setElementAtPos(self, index, val):
        self.a[index] = val

    def find(self, searchKey):
        lowerBound = 0
        upperBound = self.nElems
        while True:
            curIn = (lowerBound + upperBound) // 2

            if self.a[curIn] == searchKey:
                return curIn
            elif lowerBound > upperBound:
                return self.nElems
            else:
                if self.a[curIn] < searchKey:
                    lowerBound = curIn + 1
                else:
                    upperBound = curIn - 1

    def insert(self, value):
        lowerBound = 0
        upperBound = self.nElems - 1
        while True:
            if lowerBound > upperBound:
                break
        j = (lowerBound + upperBound) // 2
        if (value > self.a[j]):
            lowerBound = j + 1
            j += 1


arr = OrdArray()

arr.a = [1, 3, 5, 7, 9, 11]
arr.nElems = len(arr.a)

searchKey = 7
index = arr.find(searchKey)

if index != arr.nElems:
    print(f"Element {searchKey} found at index {index}.")
else:
    print(f"Element {searchKey} not found")
