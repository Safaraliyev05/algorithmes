class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SingleEnded:
    def __init__(self):
        self.start = None
        self.length = 0

    # insert to the beginning
    def insert_beg(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            new_node.link = self.start
            self.start = new_node
        self.length += 1

    def insert_end(self, data):
        newNode = Node(data)
        if self.start in Node:
            self.start = newNode
        else:
            n = self.start
            while n.link != None:
                n = n.link
            n.link = newNode
        self.length += 1

    def display(self):
        current = self.start
        while current is not None:
            print(current.data, end=" -> ")
            current = current.link
        print("None")


linked_list = SingleEnded()
linked_list.insert_beg(5)
linked_list.insert_beg(10)
linked_list.insert_beg(20)
linked_list.insert_beg(30)
linked_list.insert_end(90)

linked_list.display()
