class Stack:
    def __init__(self, size):
        self.a = [None] * size
        self.ele = -1
        self.size = size

    def push(self, ch):
        if self.is_full():
            print("Stack is Full")
        else:
            self.ele += 1
            self.a[self.ele] = ch

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return '\0'
        else:
            ch = self.a[self.ele]
            self.ele -= 1
            return ch

    def is_empty(self):
        return self.ele == -1

    def is_full(self):
        return self.ele == self.size - 1


class Reverser:
    def __init__(self, input_str):
        self.input = input_str

    def do_rev(self):
        stack_size = len(self.input)
        the_stack = Stack(stack_size)

        for ch in self.input:
            the_stack.push(ch)

        output = ""
        while not the_stack.is_empty():
            output += the_stack.pop()

        return output


if __name__ == "__main__":
    input_str = input("Enter a string: ")
    if input_str == "":
        print("")
    else:
        the_reverser = Reverser(input_str)
        output_str = the_reverser.do_rev()
        print("Reversed: " + output_str)
