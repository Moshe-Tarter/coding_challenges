class Node:
    def __init__(self, value: int = 0, next=None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f'Node with value of: {self.value}'    


def reverse(head: Node) -> Node:
    new_head = head
    temp_node = None
    while new_head:
        new_head = head.next
        head.next = temp_node
        temp_node = head
        head = new_head
        
    return temp_node

    
if __name__ == '__main__':
    head1 = Node(1, Node(2, Node(3, Node(8, Node(9)))))
    head2 = Node(4, Node(5, Node(6, Node(10, Node(11)))))
    test = reverse(head1)
    while test:
        print(test.value)
        test = test.next