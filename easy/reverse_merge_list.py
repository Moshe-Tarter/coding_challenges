class Node:
    def __init__(self, value: int = 0, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f'Node with value of: {self.value}'

def rev(head: Node) -> Node:
    current = head
    prev = None
    while current is not None:
        new_head = current.next
        current.next = prev
        prev = current
        current = new_head
    return prev


def merge(head1, head2):
    new_head = Node()
    current = new_head
    
    while head1 and head2:
        if head1.value <= head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
            
        current = current.next
            
    if head1 is None:
        current.next = head2
    else:
        current.next = head1
        
    print(new_head, current)
            
    return new_head.next
            
            
if __name__ == '__main__':
    head1 = Node(1, Node(2, Node(3, Node(8, Node(9)))))
    head2 = Node(4, Node(5, Node(6, Node(10, Node(11)))))
    new_head = merge(head1, head2)
    while new_head:
        print(new_head)
        new_head = new_head.next