"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head2 = Node(1)
head2.next = Node(8)
head2.next.next = Node(10)

merged_list = mergeTwoLists(head, head2)

curr = merged_list
while curr:
    print(curr.val, " -> " if curr.next else "", end="")
    curr = curr.next

