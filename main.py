# def moveZeroes(nums: list) -> list:
#     count = 0
#     for i, num in enumerate(nums):
#         if num == 0:
#             count += 1
#             continue
#         nums[i], nums[i - count] = nums[i - count], nums[i]
#     return nums
#
#
# print(moveZeroes([0, 1, 0, 3, 12]))
#
# 2
# def reverse(nums, i, j):
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
#
#
# def rotate(nums: list, k: int) -> list:
#     k = k % len(nums)
#     reverse(nums, 0, len(nums) - 1)
#     reverse(nums, 0, k-1)
#     reverse(nums, k, len(nums) - 1)
#     return nums
#
#
# print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
#
# 3 Pascal`s triangle
# def generate_row(prev):
#     next_ = [1]
#     for i in range(len(prev) - 1):
#         next_.append(prev[i] + prev[i + 1])
#     next_.append(1)
#     return next_
#
#
# def generate(n: int) -> list:
#     if n == 0:
#         return []
#
#     row = [1]
#     result = [row]
#
#     for i in range(n):
#         row = generate_row(row)
#         result.append(row)
#
#     return result[-1]
#
#
# print(generate(3))
#
# class Solution:
#     def generate_row(self, prev):
#         next_ = [1]
#         for i in range(len(prev) - 1):
#             next_.append(prev[i] + prev[i + 1])
#         next_.append(1)
#         return next_
#
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
#
#         row = [1]
#         result = [row]
#
#         for i in range(rowIndex):
#             row = self.generate_row(row)
#             result.append(row)
#
#         return result[-1]
#
#
# hi = Solution()
# print(hi.getRow(3))
#
#
# Two pointer
# nums = [4, 2, 1, 5, 8, 3, 6, 7]
# nums.sort()
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 8:
#             print(nums[i], nums[j])
#
# def two_pointer(nums, target):
#     nums.sort()
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         if nums[left] + nums[right] == target:
#             return True
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             right -= 1
#     return False
#
#
# def three_sum(nums, target=0):
#     nums.sort()
#     result = []
#
#     for i in range(len(nums) - 2):
#         left, right = i + 1, len(nums) - 1
#
#         while left < right:
#             if nums[i] + nums[left] + nums[right] == target:
#                 result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#             elif nums[i] + nums[left] + nums[right] < target:
#                 left += 1
#             else:
#                 right -= 1
#
#     return result
#
#
# def middle(nums, target):
#     nums.sort()  # O(N, log(N))
#     for i in range(len(nums) - 1):  # O(n)
#         left, right = i + 1, len(nums) - 1
#         while left < right:  # O(log(N))
#             mid = (left + right) // 2
#             if nums[i] + nums[mid] == target:
#                 return True
#             elif nums[i] + nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return False
#
#
# print(two_pointer([1, 3, 5, 7, 9, 11, 14], 16))
# print(three_sum([1, 3, 5, 7, 9, 11, 14], 17))
# print(middle([1, 3, 5, 7, 9, 11, 14], 20))
#
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#
#
# hi = Solution()
# hi.moveZeroes([0, 1, 0, 3,


# a = int(input("1-chi sonni kiriting: "))
# b = int(input("2-chi sonni kiriting: "))
# c = input("amallarni kiriting +, -, /, *")
# if c == "+":
#     print("Natija", a + b)
# elif c == "-":
#     print("Natija", a - b)
# elif c == "/":
#     print("Natija", a / b)
# elif c == "*":
#     print("Natija", a * b)
# else:
#     print("Bunday amallar mavjud emas")
# import flet as ft
#
# def main(page: ft.Page):
#     page.title = "Kalkulyator"
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.window_width = 300
#     page.window_height = 400
#
#     display = ft.Text(value="", size=30, text_align=ft.TextAlign.RIGHT, expand=True)
#     current_input = ""
#
#     def on_click(e):
#         nonlocal current_input
#         value = e.control.text
#
#         if value == "C":
#             current_input = ""
#         elif value == "=":
#             try:
#                 result = eval(current_input)
#                 current_input = str(result)
#             except:
#                 current_input = "Xatolik!"
#         else:
#             current_input += value
#
#         display.value = current_input
#         page.update()
#
#     def create_button(text):
#         return ft.ElevatedButton(
#             text=text, width=60, height=60, on_click=on_click
#         )
#
#     # Layout buttons like a real calculator
#     buttons = [
#         ["7", "8", "9", "/"],
#         ["4", "5", "6", "*"],
#         ["1", "2", "3", "-"],
#         ["0", "C", "=", "+"],
#     ]
#
#     grid = ft.Column()
#
#     for row in buttons:
#         row_widgets = ft.Row([create_button(btn) for btn in row], alignment=ft.MainAxisAlignment.CENTER)
#         grid.controls.append(row_widgets)
#
#     page.add(
#         ft.Container(
#             content=ft.Column([
#                 ft.Container(display, padding=10, bgcolor="#eeeeee", border_radius=10),
#                 grid
#             ]),
#             padding=20,
#             bgcolor="#f5f5f5",
#             border_radius=20,
#         )
#     )
#
# ft.app(target=main)
import tkinter as tk


def on_click(value):
    current = entry_var.get()
    if value == "C":
        entry_var.set("")
    elif value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except:
            entry_var.set("Xatolik!")
    else:
        entry_var.set(current + value)


# Create main window
root = tk.Tk()
root.title("Kalkulyator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, sticky="nsew")

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create buttons dynamically
for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2,
                        command=lambda ch=char: on_click(ch))
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

# Equal sizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the app
root.mainloop()
