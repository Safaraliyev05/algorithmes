class Swap():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap_numbers(self):
        self.x = self.x + self.y
        self.y = self.x - self.y
        self.x = self.x - self.y


swap_instance = Swap(5, 10)
print(f"x = {swap_instance.x}, y = {swap_instance.y}")

swap_instance.swap_numbers()
print(f"x = {swap_instance.x}, y = {swap_instance.y}")
