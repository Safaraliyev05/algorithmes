class Node:
    def __init__(self, key):
        self.idata = key

    def get_key(self):
        return self.idata

    def set_key(self, key):
        self.idata = key


class Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.heap_array = [None] * max_size

    def is_empty(self):
        return self.current_size == 0

    def insert(self, key):
        if self.current_size == self.max_size:
            return False
    