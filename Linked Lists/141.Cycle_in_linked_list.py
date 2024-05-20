# Given head, the head of a linked list, determine if the linked list has a cycle in it.

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def detect_cycle_linked_list(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

head = Node(1)
cycle = head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = cycle

print(detect_cycle_linked_list(head))