"""
Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Note: In the case of languages like Java, Python, and Javascript, there is no need for the deletion of objects or 
nodes because these have an automatic garbage collection mechanism that automatically identifies and reclaims memory that is no longer in use.
"""
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def removeNthFromEnd(head, n):
    number_of_elements = 0
    curr = head
    while curr:
        number_of_elements += 1
        curr = curr.next

    if n == number_of_elements:
        return head.next

    i = 1
    curr2 = head
    remove_node = number_of_elements - n
    while curr2:
        if i == remove_node:
            curr2.next = curr2.next.next
        i += 1
        curr2 = curr2.next

    return head

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, " -> " if curr.next else "", end="")
        curr = curr.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
n = 2

linked_list = removeNthFromEnd(head, n)
printLinkedList(linked_list)

