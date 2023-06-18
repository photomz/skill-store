def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    head = None
    tail = None
    for value in lst:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def linked_list_to_list(head):
    lst = []
    current = head
    while current is not None:
        lst.append(current.value)
        current = current.next
    return lst