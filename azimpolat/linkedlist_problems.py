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


def reverse(head: Node) -> Node:
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def is_same(head1: Node, head2: Node) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


def isPalindrome(head: Node) -> bool:
    middle = middleNode(head)
    middle = reverse(middle)
    return is_same(head, middle)


def mergeTwoLists(head1: Node, head2: Node) -> Node:
    curr1, curr2 = head1, head2
    head = curr = Node(0)

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next

    curr.next = curr1 or curr2

    return head.next
