# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, " -> " if curr.next else "", end="")
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reversed_linked_list = reverseLinkedList(head)
print_linked_list(reversed_linked_list)