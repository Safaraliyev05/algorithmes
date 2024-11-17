class ArraySel:
    def __init__(self, max_size):
        self.a = [0] * max_size
        self.nElems = 0

    def insert(self, value):
        if self.nElems < len(self.a):
            self.a[self.nElems] = value
            self.nElems += 1
        else:
            print("Array is full, cannot insert more elements.")

    def display(self):
        for i in range(self.nElems):
            print(self.a[i], end=" ")
        print()

    def selection_sort(self):
        for out in range(self.nElems - 1):
            min_index = out
            for in_index in range(out + 1, self.nElems):
                if self.a[in_index] < self.a[min_index]:
                    min_index = in_index
            self.swap(out, min_index)

    def swap(self, one, two):
        self.a[one], self.a[two] = self.a[two], self.a[one]


if __name__ == "__main__":
    arr = ArraySel(10)
    arr.insert(64)
    arr.insert(21)
    arr.insert(33)
    arr.insert(70)
    arr.insert(12)
    arr.insert(85)
    arr.insert(44)
    arr.insert(3)
    arr.insert(99)
    arr.insert(0)

    print("Before sorting:")
    arr.display()

    arr.selection_sort()

    print("After sorting:")
    arr.display()
