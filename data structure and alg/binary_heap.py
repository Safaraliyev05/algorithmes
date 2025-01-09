class Node:
    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key


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
        new_node = Node(key)
        self.heap_array[self.current_size] = new_node
        self.trickle_up(self.current_size)
        self.current_size += 1
        return True

    def trickle_up(self, index):
        parent = (index - 1) // 2
        bottom = self.heap_array[index]
        while index > 0 and self.heap_array[parent].get_key() > bottom.get_key():
            self.heap_array[index] = self.heap_array[parent]
            index = parent
            parent = (parent - 1) // 2
        self.heap_array[index] = bottom

    def remove(self):
        if self.is_empty():
            return None
        root = self.heap_array[0]
        self.current_size -= 1
        self.heap_array[0] = self.heap_array[self.current_size]
        self.trickle_down(0)
        return root

    def trickle_down(self, index):
        top = self.heap_array[index]
        while index < self.current_size // 2:
            left_child = 2 * index + 1
            right_child = left_child + 1

            if (right_child < self.current_size and
                    self.heap_array[left_child].get_key() > self.heap_array[right_child].get_key()):
                smaller_child = right_child
            else:
                smaller_child = left_child

            if top.get_key() <= self.heap_array[smaller_child].get_key():
                break

            self.heap_array[index] = self.heap_array[smaller_child]
            index = smaller_child

        self.heap_array[index] = top

    def change(self, index, new_value):
        if index < 0 or index >= self.current_size:
            return False
        old_value = self.heap_array[index].get_key()
        self.heap_array[index].set_key(new_value)

        if old_value < new_value:
            self.trickle_up(index)
        else:
            self.trickle_down(index)
        return True

    def display_heap(self):
        print("Heap array:", end=" ")
        for i in range(self.current_size):
            print(self.heap_array[i].get_key(), end=" ")
        print()

        n_blanks = 32
        items_per_row = 1
        column = 0
        j = 0
        dots = "." * 64
        print(dots)

        while self.current_size > 0:
            if column == 0:
                print(" " * n_blanks, end="")

            print(self.heap_array[j].get_key(), end="")
            j += 1

            if j == self.current_size:
                break

            column += 1
            if column == items_per_row:
                n_blanks //= 2
                items_per_row *= 2
                column = 0
                print()
            else:
                print(" " * (n_blanks * 2 - 2), end="")

        print(f"\n{dots}")


if __name__ == "__main__":
    heap = Heap(31)

    heap.insert(70)
    heap.insert(40)
    heap.insert(50)
    heap.insert(20)
    heap.insert(60)
    heap.insert(100)
    heap.insert(80)
    heap.insert(30)
    heap.insert(10)
    heap.insert(90)

    while True:
        choice = input("Enter first letter of show, insert, remove, change: ").strip().lower()

        if choice == 's':
            heap.display_heap()

        elif choice == 'i':
            value = int(input("Enter value to insert: "))
            if not heap.insert(value):
                print("Can't insert; heap full")

        elif choice == 'r':
            if not heap.is_empty():
                removed = heap.remove()
                print(f"Removed: {removed.get_key()}")
            else:
                print("Can't remove; heap empty")

        elif choice == 'c':
            index = int(input("Enter current index of item: "))
            new_value = int(input("Enter new key: "))
            if not heap.change(index, new_value):
                print("Invalid index")

        else:
            print("Invalid entry\n"
                  "s for show\n"
                  "i for insert\n"
                  "r for remove\n"
                  "c for change\n")
