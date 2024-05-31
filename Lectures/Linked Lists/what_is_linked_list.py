class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.dummy_head = ListNode()  # Create a dummy head node
    
    def insert_at_beginning(self, value):
        new_node = ListNode(value)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
    
    def delete_node(self, value):
        prev = self.dummy_head
        current = self.dummy_head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
    
    def display(self):
        current = self.dummy_head.next  # Skip the dummy head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

# Example Usage
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.display()  # Output: 3 -> 2 -> 1 -> None
ll.delete_node(2)
ll.display()  # Output: 3 -> 1 -> None

