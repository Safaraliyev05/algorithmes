class Queue:
    def __init__(self, max_size):
        self.max = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.max - 1

    def is_empty(self):
        return self.front == -1

    def insert(self, val):
        if self.is_full():
            print("Overflow")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = val

    def delete(self):
        if self.is_empty():
            print("Underflow")
        else:
            print(f"Deleted: {self.queue[self.front]}")
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue[self.front:self.rear + 1])


class QueueApp:
    def main(self):
        q = Queue(10)
        q.insert(10)
        q.insert(20)
        q.insert(30)
        q.insert(40)
        q.insert(50)
        q.insert(60)
        q.display()
        q.delete()
        q.display()


if __name__ == "__main__":
    app = QueueApp()
    app.main()
