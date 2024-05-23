"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def reorderList(head):
    linked_values = []
    curr = head
    while curr:
        linked_values.append(curr)
        curr = curr.next
    print(linked_values)

    l, r = 0, len(linked_values) - 1
    dummy = Node(0)
    curr = dummy

    while l <= r:
        if l == r: #Handling odd numbers
            curr.next = linked_values[l]
            curr = curr.next
            break
        curr.next = linked_values[l]
        curr = curr.next
        curr.next = linked_values[r]
        curr = curr.next
        l += 1
        r -= 1

    curr.next = None
    # Print the reordered list
    curr = dummy.next
    while curr:
        print(curr.val, "->" if curr.next else "", end=" ")
        curr = curr.next
    
    return dummy.next
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(reorderList(head))

