class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def middleNode(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


print(middleNode([1, 2, 3, 4, 5]))
print(middleNode(head=[1, 2, 3, 4, 5, 6]))
